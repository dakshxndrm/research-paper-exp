"""Arm B -- the proposed OKF-RAG retriever.

Differences from the baseline, each mapped to a hallucination cause:

  concept-level units      -> no fact split across a chunk boundary
  embed title+description  -> retrieval matches the concept's purpose, not
                              incidental wording deep in the body
  1-hop link expansion     -> multi-hop questions get their dependency concept
                              even when it does not match the query lexically
  provenance headers       -> every block carries its concept path for citation

Each of these can be switched off independently for the ablation study.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Set

import yaml

from src.config import estimate_tokens
from src.embeddings import DenseIndex


class Concept:
    def __init__(self, path: str, meta: Dict[str, Any], body: str, links: List[str]):
        self.path = path
        self.type = str(meta.get("type", "Concept"))
        self.title = str(meta.get("title", path))
        self.description = str(meta.get("description", ""))
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
    return [t.lstrip("/") for t in re.findall(r"\]\((/[^)\s]+\.md)\)", body)]


FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def split_frontmatter(text: str) -> tuple[Dict[str, Any], str]:
    """Split `---\\nyaml\\n---\\nbody`. write_bundle emits exactly this shape.

    Line-anchored on purpose: a bare `str.split("---")` would also fire on a
    horizontal rule or an em-dash run inside a concept body.
    """
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text.strip()
    return yaml.safe_load(m.group(1)) or {}, text[m.end():].strip()


def load_bundle(bundle_dir: Path) -> List[Concept]:
    concepts: List[Concept] = []
    for path in sorted(bundle_dir.rglob("*.md")):
        rel = str(path.relative_to(bundle_dir)).replace("\\", "/")
        meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
        concepts.append(Concept(rel, meta, body, parse_links(body)))
    if not concepts:
        raise SystemExit(f"No concepts found in {bundle_dir}. Run build_bundle.py first.")
    return concepts


class OKFRag:
    def __init__(self, cfg: Dict[str, Any], overrides: Dict[str, Any] | None = None):
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

    def _expansion_status(self, seed_ids: List[int], expanded_ids: List[int],
                          n_expanded_used: int) -> str:
        """Explain why expansion contributed what it did.

        n_expanded == 0 conflates genuinely different failures, and they call for
        opposite fixes: no_links means the bundle's link graph is empty (fix the
        linker), all_redundant means retrieval already covers the neighbourhood
        (a small-corpus artefact), budget_blocked means the context budget is the
        binding constraint (fix the budget).
        """
        if self.hop <= 0:
            return "disabled"          # the no_expansion ablation
        resolvable = {
            self.by_path[link]
            for idx in seed_ids
            for link in self.concepts[idx].links
            if link in self.by_path
        }
        if not resolvable:
            return "no_links"
        if not expanded_ids:
            return "all_redundant"     # every target was already retrieved as a seed
        if n_expanded_used == 0:
            return "budget_blocked"    # found new concepts, none survived the budget
        return "expanded"

    def retrieve(self, question: str) -> Dict[str, Any]:
        hits = self.index.search(question, self.top_k)
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

        n_expanded_used = len([i for i in expanded_ids if self.concepts[i].path in used])
        return {
            "context": "\n\n---\n\n".join(blocks),
            "retrieved_ids": used,
            "n_units": len(used),
            "n_seed": len([i for i in seed_ids if self.concepts[i].path in used]),
            "n_expanded": n_expanded_used,
            "expansion_status": self._expansion_status(seed_ids, expanded_ids, n_expanded_used),
            "context_tokens": spent,
        }

    @property
    def unit_count(self) -> int:
        return len(self.concepts)
