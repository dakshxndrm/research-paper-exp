"""Stage 1 -- build an OKF v0.1 bundle from a raw document corpus.

Two-pass design, deliberately:

  Pass 1 (LLM-assisted): split each raw document into self-contained CONCEPTS.
          Each concept becomes one markdown file with YAML frontmatter carrying
          the OKF reserved fields (type, title, description, resource, tags,
          timestamp).

  Pass 2 (fully deterministic): cross-link concepts by exact title / alias
          matching in each body, then emit index.md files per directory.

Why pass 2 is not LLM-driven: cross-linking is the mechanism the paper claims
credit for. Making it rule-based means it is reproducible, auditable, and
cannot be accused of leaking answers via a smarter model. State this in the
paper's implementation section.

Usage:
    python -m src.build_bundle
    python -m src.build_bundle --limit 5        # smoke test on 5 docs
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import yaml
from tqdm import tqdm

from src.config import ensure_dir, load_config, set_seed
from src.llm import LLMClient, extract_json

EXTRACT_SYSTEM = """You are a knowledge engineer building an Open Knowledge Format (OKF) bundle.

You split a source document into CONCEPTS. A concept is one self-contained idea,
entity, rule, procedure, or definition that a reader could understand on its own
without the surrounding document.

Rules:
- Each concept must be self-contained. Never write "as mentioned above" or "see
  the previous section". Restate what is needed.
- Do NOT invent facts. Every sentence in a concept body must be supported by the
  source document. If the source is silent on something, omit it.
- Preserve specific numbers, dates, names, codes, and thresholds exactly.
- Prefer 4-12 concepts per document. Merge trivia into a larger concept rather
  than creating a stub.

Return ONLY a JSON array. No prose, no markdown fences. Each element:
{
  "type":        "<short noun phrase, e.g. Policy, Definition, Procedure, Entity, Metric>",
  "title":       "<short unique title, 2-6 words>",
  "description": "<one sentence describing what this concept covers>",
  "tags":        ["<lowercase-tag>", "..."],
  "body":        "<markdown body, the full substance of the concept>"
}"""

EXTRACT_USER = """Source document filename: {filename}

--- BEGIN DOCUMENT ---
{document}
--- END DOCUMENT ---

Split this document into at most {max_concepts} self-contained concepts.
Return only the JSON array."""


def slugify(text: str) -> str:
    """Turn a concept title into a stable filename stem."""
    s = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    s = re.sub(r"[\s-]+", "_", s)
    return s[:60] or "concept"


IRREGULAR_PLURALS = {
    "criterion": "criteria",
    "index": "indices",
    "datum": "data",
    "analysis": "analyses",
}


def pluralise(word: str) -> str:
    """Folder names read better pluralised: Policy -> policies, Entity -> entities."""
    lower = word.lower()
    if lower in IRREGULAR_PLURALS:
        return IRREGULAR_PLURALS[lower]
    if word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    return word + "s"


def read_raw_docs(raw_dir: Path, limit: int | None = None) -> List[Path]:
    docs = sorted(
        p for p in raw_dir.rglob("*") if p.suffix.lower() in {".md", ".txt"} and p.is_file()
    )
    if not docs:
        raise SystemExit(
            f"No .md or .txt files found in {raw_dir}.\n"
            f"Put your corpus there first (see README, Step 1)."
        )
    return docs[:limit] if limit else docs


# --------------------------------------------------------------------------- #
# Pass 1 -- concept extraction
# --------------------------------------------------------------------------- #


def extract_concepts(doc_path: Path, client: LLMClient, max_concepts: int,
                     min_words: int, debug_dir: Path | None = None) -> List[Dict[str, Any]]:
    text = doc_path.read_text(encoding="utf-8", errors="ignore")
    if not text.strip():
        return []

    raw = client.generate(
        EXTRACT_SYSTEM,
        EXTRACT_USER.format(
            filename=doc_path.name, document=text, max_concepts=max_concepts
        ),
    )

    if debug_dir is not None:
        (debug_dir / f"{doc_path.stem}.raw.txt").write_text(raw, encoding="utf-8")

    try:
        concepts = extract_json(raw)
    except Exception as exc:  # noqa: BLE001 -- log and skip, do not kill the run
        tqdm.write(f"  [warn] {doc_path.name}: JSON parse failed ({exc}). "
                   f"Raw response saved to debug/ for inspection.")
        return []

    if not isinstance(concepts, list):
        tqdm.write(f"  [warn] {doc_path.name}: LLM did not return a JSON array. Skipped.")
        return []

    cleaned: List[Dict[str, Any]] = []
    dropped_short = 0
    for c in concepts:
        if not isinstance(c, dict) or not c.get("title") or not c.get("body"):
            continue
        if len(str(c["body"]).split()) < min_words:
            dropped_short += 1
            continue
        cleaned.append(
            {
                "type": str(c.get("type", "Concept")).strip(),
                "title": str(c["title"]).strip(),
                "description": str(c.get("description", "")).strip(),
                "tags": [str(t).strip().lower() for t in c.get("tags", []) if str(t).strip()],
                "body": str(c["body"]).strip(),
                "source_doc": doc_path.name,
            }
        )

    tqdm.write(
        f"  {doc_path.name}: {len(concepts)} raw -> {len(cleaned)} kept "
        f"({dropped_short} dropped for being under {min_words} words)"
    )
    if not cleaned:
        tqdm.write(f"  [warn] {doc_path.name}: ZERO concepts survived. "
                   f"Check debug/{doc_path.stem}.raw.txt")
    return cleaned


# --------------------------------------------------------------------------- #
# Pass 2 -- deterministic cross-linking
# --------------------------------------------------------------------------- #


MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")


def _first_free_match(pattern: re.Pattern, body: str) -> re.Match | None:
    """First match that is not already inside an existing markdown link.

    Without this, a short title ("Attendance") matches inside a longer title's
    already-inserted link text ("[Medical Attendance Exemption](/...)") and
    produces nested, broken markdown that corrupts both the rendered concept and
    its parsed link list.
    """
    spans = [m.span() for m in MARKDOWN_LINK.finditer(body)]
    for m in pattern.finditer(body):
        if not any(m.start() < end and m.end() > start for start, end in spans):
            return m
    return None


def cross_link(concepts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Insert markdown links wherever one concept's body mentions another's title.

    Longest titles are matched first so that "Late Fee Waiver Policy" wins over
    "Late Fee". Each target is linked at most once per body to avoid link spam.
    """
    by_title = {c["title"]: c for c in concepts}
    ordered_titles = sorted(by_title, key=len, reverse=True)

    for concept in concepts:
        body = concept["body"]
        linked_targets: List[str] = []

        for title in ordered_titles:
            if title == concept["title"]:
                continue
            target = by_title[title]
            # Word-boundary, case-insensitive, skip text already inside a link.
            pattern = re.compile(rf"(?<!\[)\b{re.escape(title)}\b(?!\])", re.IGNORECASE)
            match = _first_free_match(pattern, body)
            if not match:
                continue
            rel = f"/{target['rel_path']}"
            body = (
                body[: match.start()]
                + f"[{match.group(0)}]({rel})"
                + body[match.end() :]
            )
            linked_targets.append(target["rel_path"])

        concept["body"] = body
        concept["links"] = linked_targets

    return concepts


# --------------------------------------------------------------------------- #
# Writing the bundle
# --------------------------------------------------------------------------- #


def assign_paths(concepts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Give every concept a unique bundle-relative path: <type_slug>/<title_slug>.md"""
    seen: Dict[str, int] = {}
    for c in concepts:
        folder = pluralise(slugify(c["type"]))
        stem = slugify(c["title"])
        key = f"{folder}/{stem}"
        if key in seen:
            seen[key] += 1
            stem = f"{stem}_{seen[key]}"
        else:
            seen[key] = 0
        c["rel_path"] = f"{folder}/{stem}.md"
    return concepts


def write_bundle(concepts: List[Dict[str, Any]], bundle_dir: Path) -> None:
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    ensure_dir(bundle_dir)

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    for c in concepts:
        out = bundle_dir / c["rel_path"]
        ensure_dir(out.parent)
        frontmatter = {
            "type": c["type"],                 # the one required OKF field
            "title": c["title"],
            "description": c["description"],
            "resource": f"source://{c['source_doc']}",
            "tags": c["tags"],
            "timestamp": timestamp,
        }
        fm = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
        out.write_text(f"---\n{fm}\n---\n\n{c['body']}\n", encoding="utf-8")

    _write_indexes(concepts, bundle_dir)
    _write_log(concepts, bundle_dir, timestamp)


def _write_indexes(concepts: List[Dict[str, Any]], bundle_dir: Path) -> None:
    """Emit index.md per folder plus a root index -- OKF progressive disclosure."""
    folders: Dict[str, List[Dict[str, Any]]] = {}
    for c in concepts:
        folders.setdefault(c["rel_path"].split("/")[0], []).append(c)

    for folder, items in folders.items():
        lines = [f"---\ntype: Index\ntitle: {folder}\n---\n", f"# {folder}\n"]
        for c in sorted(items, key=lambda x: x["title"]):
            name = c["rel_path"].split("/")[1]
            lines.append(f"- [{c['title']}]({name}) — {c['description']}")
        (bundle_dir / folder / "index.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )

    root = ["---\ntype: Index\ntitle: Bundle Root\n---\n", "# Bundle Root\n"]
    for folder in sorted(folders):
        root.append(f"- [{folder}]({folder}/index.md) — {len(folders[folder])} concepts")
    (bundle_dir / "index.md").write_text("\n".join(root) + "\n", encoding="utf-8")


def _write_log(concepts: List[Dict[str, Any]], bundle_dir: Path, ts: str) -> None:
    lines = ["# Change log\n", f"## {ts}\n", f"- Initial bundle build: {len(concepts)} concepts.\n"]
    (bundle_dir / "log.md").write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------- #


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an OKF bundle from raw docs.")
    parser.add_argument("--limit", type=int, default=None, help="Only process N docs.")
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    set_seed(cfg["experiment"]["seed"])

    raw_dir = Path(cfg["paths"]["raw_docs"])
    bundle_dir = Path(cfg["paths"]["bundle"])
    bcfg = cfg["bundle_builder"]

    client = LLMClient(
        {
            "provider": bcfg["provider"],
            "model": bcfg["model"],
            "temperature": bcfg["temperature"],
            "max_tokens": 4000,
            "base_url": cfg["generation"]["base_url"],
            "api_key_env": cfg["generation"]["api_key_env"],
        }
    )

    docs = read_raw_docs(raw_dir, args.limit)
    print(f"Extracting concepts from {len(docs)} documents...")

    debug_dir = ensure_dir(Path(cfg["paths"]["results"]) / "bundle_debug")
    all_concepts: List[Dict[str, Any]] = []
    for doc in tqdm(docs):
        all_concepts.extend(
            extract_concepts(
                doc, client, bcfg["max_concepts_per_doc"], bcfg["min_concept_words"],
                debug_dir,
            )
        )

    if not all_concepts:
        raise SystemExit("No concepts extracted. Check the LLM provider is reachable.")

    all_concepts = assign_paths(all_concepts)
    all_concepts = cross_link(all_concepts)
    write_bundle(all_concepts, bundle_dir)

    n_links = sum(len(c["links"]) for c in all_concepts)
    stats = {
        "documents": len(docs),
        "concepts": len(all_concepts),
        "cross_links": n_links,
        "avg_links_per_concept": round(n_links / len(all_concepts), 2),
        "avg_body_words": round(
            sum(len(c["body"].split()) for c in all_concepts) / len(all_concepts), 1
        ),
    }
    ensure_dir(cfg["paths"]["results"])
    (Path(cfg["paths"]["results"]) / "bundle_stats.json").write_text(
        json.dumps(stats, indent=2), encoding="utf-8"
    )

    print(f"\nBundle written to {bundle_dir}")
    print(json.dumps(stats, indent=2))
    print("\nReport these stats in the paper's dataset section.")


if __name__ == "__main__":
    main()
