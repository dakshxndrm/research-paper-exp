"""Arm B -- the proposed OKF-RAG retriever.

Differences from the baseline, each mapped to a hallucination cause:

  concept-level units      -> no fact split across a chunk boundary
  embed title+description  -> retrieval matches the concept's purpose, not
                              incidental wording deep in the body
  metadata pre-filter      -> freshness / tag scoping via YAML frontmatter
  1-hop link expansion     -> multi-hop questions get their dependency concept
                              even when it does not match the query lexically
  provenance headers       -> every block carries its concept path for citation

Each of these can be switched off independently for the ablation study.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Set

import frontmatter

from src.config import estimate_tokens
from src.embeddings import DenseIndex


class Concept:
    __slots__ = ("path", "type", "title", "description", "tags", "timestamp", "body", "links")

    def __init__(self, path: str, meta: Dict[str, Any], body: str, links: List[str]):
        self.path = path
        self.type = str(meta.get("type", "Concept"))
        self.title = str(meta.get("title", path))
        self.description = str(meta.get("description", ""))
        self.tags = [str(t).lower() for t in (meta.get("tags") or [])]
        self.timestamp = meta.get("timestamp")
        self.body = body
        self.links = links

    def embed_text(self, field: str) -> str:
        if field == "full_body":
            return f"{self.title}. {self.description}\n{self.body}"
        return f"{self.title}. {self.description}"

    def render(self) -> str:
        return f"[concept: /{self.path}] ({self.type})\n{self.title}\n\n{self.body}"


def parse_links(body: str) -> List[str]:
    """Extract bundle-relative markdown link targets from a concept body."""
    import re

    return [t.lstrip("/") for t in re.findall(r"\]\((/[^)\s]+\.md)\)", body)]


def load_bundle(bundle_dir: Path) -> List[Concept]:
    concepts: List[Concept] = []
    for path in sorted(bundle_dir.rglob("*.md")):
        rel = str(path.relative_to(bundle_dir)).replace("\\", "/")
        if rel.endswith("index.md") or rel == "log.md":
            continue  # index/log are routing aids, not answerable concepts
        post = frontmatter.load(path)
        concepts.append(Concept(rel, post.metadata, post.content.strip(), parse_links(post.content)))
    if not concepts:
        raise SystemExit(f"No concepts found in {bundle_dir}. Run build_bundle.py first.")
    return concepts


class OKFRag:
    def __init__(self, cfg: Dict[str, Any], overrides: Dict[str, Any] | None = None):
        self.cfg = cfg
        oc = dict(cfg["retrieval"]["okf"])
        oc.update(overrides or {})          # ablation switches land here
        self.oc = oc

        self.top_k = oc["top_k"]
        self.hop = oc["hop_expansion"]
        self.max_expanded = oc["max_expanded"]
        self.budget = cfg["retrieval"]["context_token_budget"]

        self.concepts = load_bundle(Path(cfg["paths"]["bundle"]))
        self.by_path = {c.path: i for i, c in enumerate(self.concepts)}

        self.index = DenseIndex(
            [c.embed_text(oc["embed_field"]) for c in self.concepts],
            cfg["embedding"]["model"],
            cfg["embedding"]["batch_size"],
        )

    # ------------------------------------------------------------------ #

    def _allowed_ids(self) -> List[int] | None:
        """Metadata pre-filter using OKF frontmatter (freshness)."""
        if not self.oc.get("use_freshness_filter"):
            return None
        cutoff = datetime.now(timezone.utc) - timedelta(
            days=self.oc.get("freshness_max_age_days", 3650)
        )
        allowed: List[int] = []
        for i, c in enumerate(self.concepts):
            ts = c.timestamp
            if ts is None:
                allowed.append(i)
                continue
            if isinstance(ts, str):
                try:
                    ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                except ValueError:
                    allowed.append(i)
                    continue
            if isinstance(ts, datetime):
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                if ts >= cutoff:
                    allowed.append(i)
            else:
                allowed.append(i)
        return allowed

    def _expand(self, seed_ids: List[int]) -> List[int]:
        """Follow markdown cross-links `hop` levels out from the seed concepts."""
        if self.hop <= 0:
            return []
        frontier: Set[int] = set(seed_ids)
        seen: Set[int] = set(seed_ids)
        added: List[int] = []

        for _ in range(self.hop):
            next_frontier: Set[int] = set()
            for idx in frontier:
                for link in self.concepts[idx].links:
                    tgt = self.by_path.get(link)
                    if tgt is None or tgt in seen:
                        continue
                    seen.add(tgt)
                    next_frontier.add(tgt)
                    added.append(tgt)
                    if len(added) >= self.max_expanded:
                        return added
            frontier = next_frontier
            if not frontier:
                break
        return added

    # ------------------------------------------------------------------ #

    def retrieve(self, question: str) -> Dict[str, Any]:
        hits = self.index.search(question, self.top_k, self._allowed_ids())
        seed_ids = [i for i, _ in hits]
        expanded_ids = self._expand(seed_ids)

        # Seeds first (higher relevance), then link-expanded neighbours.
        blocks: List[str] = []
        used: List[str] = []
        spent = 0
        for idx in seed_ids + expanded_ids:
            concept = self.concepts[idx]
            block = concept.render()
            cost = estimate_tokens(block)
            if spent + cost > self.budget:
                continue
            blocks.append(block)
            used.append(concept.path)
            spent += cost

        return {
            "context": "\n\n---\n\n".join(blocks),
            "retrieved_ids": used,
            "n_units": len(used),
            "n_seed": len([i for i in seed_ids if self.concepts[i].path in used]),
            "n_expanded": len([i for i in expanded_ids if self.concepts[i].path in used]),
            "context_tokens": spent,
            "scores": [round(s, 4) for _, s in hits],
        }

    @property
    def unit_count(self) -> int:
        return len(self.concepts)
