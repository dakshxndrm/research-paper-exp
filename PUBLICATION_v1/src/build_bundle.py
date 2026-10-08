"""Stage 1 -- build an OKF v0.1 bundle from a raw document corpus.

Two-pass design, deliberately:

  Pass 1 (LLM-assisted): split each raw document into self-contained CONCEPTS.
          Each concept becomes one markdown file with YAML frontmatter carrying
          the OKF reserved fields (type, title, description, resource, tags,
          timestamp).

  Pass 2 (fully deterministic): cross-link concepts by exact title / alias
          matching in each body.

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
import csv
import json
import re
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import yaml
from tqdm import tqdm

from src.config import load_config, set_seed
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
  "aliases":     ["<other surface form>", "..."],
  "tags":        ["<lowercase-tag>", "..."],
  "body":        "<markdown body, the full substance of the concept>"
}

About "aliases": list every natural-language phrase that a DIFFERENT concept's
body would plausibly use to refer to this concept -- role names, short forms,
form numbers, and above all the exact wording the source document itself uses.
A concept titled "Medical Exemption Review and Approval" should list aliases
such as "medical exemption", "exemption process", "Form MX-2".

Aliases must be phrases that actually appear in, or are directly implied by,
the source document. Do NOT invent synonyms the document would never use. Omit
generic words that would match unrelated text ("the process", "the student").
Use an empty list if nothing fits."""

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

    # ponytail: the per-doc .concepts.json IS the checkpoint -- no separate
    # ledger to keep in sync. A run that dies on doc 9 resumes at doc 9.
    # It is keyed on filename only, so it goes STALE if you change the document
    # or bundle_builder's extraction settings: delete the file (or the whole
    # bundle_debug dir) to force re-extraction.
    ckpt = debug_dir / f"{doc_path.stem}.concepts.json" if debug_dir else None
    if ckpt is not None and ckpt.exists():
        cached = json.loads(ckpt.read_text(encoding="utf-8"))
        tqdm.write(f"  {doc_path.name}: {len(cached)} concepts from checkpoint (skipped)")
        return cached

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
        title = str(c["title"]).strip()
        raw_aliases = c.get("aliases") or []
        if isinstance(raw_aliases, str):        # model occasionally returns a bare string
            raw_aliases = [raw_aliases]
        aliases: List[str] = []
        for a in raw_aliases:
            a = str(a).strip()
            # A one-word alias matches far too much text; an alias equal to the
            # title is already covered by title matching.
            if len(a) < 4 or a.lower() == title.lower():
                continue
            if a.lower() not in {x.lower() for x in aliases}:
                aliases.append(a)

        cleaned.append(
            {
                "type": str(c.get("type", "Concept")).strip(),
                "title": title,
                "description": str(c.get("description", "")).strip(),
                "aliases": aliases,
                "tags": [str(t).strip().lower() for t in c.get("tags", []) if str(t).strip()],
                "body": str(c["body"]).strip(),
                "source_doc": doc_path.name,
            }
        )

    if not raw.rstrip().endswith("]"):
        # extract_json salvaged the complete objects, but the tail was cut off:
        # the concepts after the truncation point are gone. Say so.
        tqdm.write(f"  [warn] {doc_path.name}: response was TRUNCATED (hit max_tokens). "
                   f"Kept the complete concepts only -- raise bundle_builder.max_tokens.")

    tqdm.write(
        f"  {doc_path.name}: {len(concepts)} raw -> {len(cleaned)} kept "
        f"({dropped_short} dropped for being under {min_words} words)"
    )
    if not cleaned:
        tqdm.write(f"  [warn] {doc_path.name}: ZERO concepts survived. "
                   f"Check debug/{doc_path.stem}.raw.txt")
    elif ckpt is not None:
        # Only checkpoint a real result -- an empty one would permanently mask
        # a document that failed to extract.
        ckpt.write_text(json.dumps(cleaned, indent=2), encoding="utf-8")
    return cleaned


# --------------------------------------------------------------------------- #
# Pass 2 -- deterministic cross-linking
# --------------------------------------------------------------------------- #


LINK_MODES = ("title_only", "alias")


def count_ambiguous_aliases(concepts: List[Dict[str, Any]], link_mode: str) -> int:
    """Aliases claimed by two or more concepts. Reported, never acted on.

    A phrase two concepts both claim identifies neither, so this is the scale of
    the ambiguity problem in the extractor's aliases. Shared family vocabulary is
    ambiguous by this test yet still produces correct links, so dropping it would
    trade away real recall -- if you ever do want to filter, this is where it goes.
    title_only never consults aliases, so it always scores 0.
    """
    if link_mode == "title_only":
        return 0
    owners = Counter(
        " ".join(a.lower().split()) for c in concepts for a in c.get("aliases", [])
    )
    return sum(n > 1 for n in owners.values())


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


def cross_link(concepts: List[Dict[str, Any]],
               link_mode: str = "title_only") -> List[Dict[str, Any]]:
    """Insert markdown links wherever one concept's body mentions another concept.

    Longest surface forms are matched first so that "Late Fee Waiver Policy" wins
    over "Late Fee". Each target is linked at most once per body to avoid spam.

    link_mode:
      "title_only"    -- match concept titles only (the original behaviour)
      "alias"         -- titles plus the extractor's recorded aliases

    All modes are pure rule-based string matching: word-boundary,
    case-insensitive, longest-first, deterministic, no LLM call. Aliases are
    generated during extraction (pass 1); using them here does not make the
    linking step itself model-dependent, so the auditability guarantee holds.
    """
    if link_mode not in LINK_MODES:
        raise SystemExit(f"Unknown link_mode {link_mode!r}. Use one of {LINK_MODES}.")

    # surface form -> (target concept, is_alias)
    surfaces: Dict[str, tuple] = {}
    for c in concepts:
        surfaces.setdefault(c["title"], (c, False))
    if link_mode != "title_only":
        for c in concepts:
            for alias in c.get("aliases", []):
                # A title always wins over another concept's alias.
                if alias not in surfaces:
                    surfaces[alias] = (c, True)

    ordered = sorted(surfaces, key=len, reverse=True)

    for concept in concepts:
        body = concept["body"]
        linked_targets: List[str] = []
        alias_hits = 0
        details: List[Dict[str, str]] = []

        for surface in ordered:
            target, is_alias = surfaces[surface]
            if target["rel_path"] == concept["rel_path"]:
                continue                        # never link a concept to itself
            if target["rel_path"] in linked_targets:
                continue                        # already linked via another surface form
            # Word-boundary, case-insensitive, skip text already inside a link.
            pattern = re.compile(rf"(?<!\[)\b{re.escape(surface)}\b(?!\])", re.IGNORECASE)
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
            alias_hits += int(is_alias)
            details.append(
                {
                    "source_concept": concept["rel_path"],
                    "target_concept": target["rel_path"],
                    "matched_phrase": match.group(0),
                    "match_type": "alias" if is_alias else "title",
                }
            )

        concept["body"] = body
        concept["links"] = linked_targets
        concept["links_from_alias"] = alias_hits
        concept["link_details"] = details

    return concepts


# --------------------------------------------------------------------------- #
# Writing the bundle
# --------------------------------------------------------------------------- #


def assign_paths(concepts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Give every concept a unique bundle-relative path: <type_slug>/<title_slug>.md"""
    seen: Dict[str, int] = {}
    for c in concepts:
        folder = slugify(c["type"])
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
    bundle_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    for c in concepts:
        out = bundle_dir / c["rel_path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        frontmatter = {
            "type": c["type"],                 # the one required OKF field
            "title": c["title"],
            "description": c["description"],
            "resource": f"source://{c['source_doc']}",
            "tags": c["tags"],
            "timestamp": timestamp,
        }
        if c.get("aliases"):                   # optional -- omitted when empty
            frontmatter["aliases"] = c["aliases"]
        fm = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
        out.write_text(f"---\n{fm}\n---\n\n{c['body']}\n", encoding="utf-8")


AUDIT_COLUMNS = ["source_concept", "target_concept", "matched_phrase", "match_type", "verdict"]


def _write_link_audit(concepts: List[Dict[str, Any]], results_dir: Path,
                      link_mode: str) -> Path:
    """Write every cross-link with a `verdict` column for manual grading.

    Link *recall* is measurable automatically; link *precision* is not -- only a
    human can say whether "Head of Department" pointing at a medical-exemption
    concept is a real relationship or an artefact of a too-generic alias. Fill
    `verdict` with correct/spurious/borderline, then run scripts/link_precision.py.

    Named per link_mode so the two builds cannot clobber each other, and any
    verdict already graded for an identical link is carried forward -- grading
    1,103 links by hand is hours of work that a rebuild must never silently
    destroy. A link whose phrase or endpoints changed is re-graded from blank.
    """
    path = results_dir / f"link_audit_{link_mode}.csv"

    graded: Dict[tuple, str] = {}
    if path.exists():
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if (row.get("verdict") or "").strip():
                    graded[tuple(row[k] for k in AUDIT_COLUMNS[:4])] = row["verdict"]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=AUDIT_COLUMNS)
        writer.writeheader()
        for c in concepts:
            for d in c.get("link_details", []):
                key = tuple(str(d[k]) for k in AUDIT_COLUMNS[:4])
                writer.writerow({**d, "verdict": graded.get(key, "")})
    if graded:
        print(f"  carried forward {len(graded)} existing verdict(s) into {path.name}")
    return path


# --------------------------------------------------------------------------- #


def make_client(cfg: Dict[str, Any]) -> LLMClient:
    """The extraction client. Shared so scripts/bundle_variance.py cannot drift."""
    bcfg = cfg["bundle_builder"]
    return LLMClient(
        {
            "model": bcfg["model"],
            "temperature": bcfg["temperature"],
            "max_tokens": bcfg.get("max_tokens", 8000),
            # Fall back to generation.* so an unswitched config behaves as
            # before, but let bundle_builder override the provider on its own
            # -- this stage has its own quota problem and its own model.
            "base_url": bcfg.get("base_url", cfg["generation"]["base_url"]),
            "api_key_env": bcfg.get("api_key_env", cfg["generation"]["api_key_env"]),
            "chat_path": bcfg.get("chat_path", "/v1/chat/completions"),
            "seed": bcfg.get("seed"),
            "send_seed": bcfg.get("send_seed", True),
            "timeout_s": bcfg.get("timeout_s", 180),
            "retries": bcfg.get("retries", 3),
            "max_retry_after_s": bcfg.get("max_retry_after_s", 120),
        }
    )


def build_concepts(cfg: Dict[str, Any], limit: int | None = None,
                   debug_dir: Path | None = None) -> tuple[List[Dict[str, Any]], int]:
    """Raw docs -> extracted, path-assigned, cross-linked concepts.

    Everything up to (not including) writing the bundle. Returns
    (concepts, n_documents). bundle_variance.py reuses this so a rebuild it
    measures is the same rebuild build_bundle does.
    """
    bcfg = cfg["bundle_builder"]
    client = make_client(cfg)
    docs = read_raw_docs(Path(cfg["paths"]["raw_docs"]), limit)
    print(f"Extracting concepts from {len(docs)} documents...")

    concepts: List[Dict[str, Any]] = []
    for doc in tqdm(docs):
        concepts.extend(
            extract_concepts(
                doc, client, bcfg["max_concepts_per_doc"], bcfg["min_concept_words"],
                debug_dir,
            )
        )
    if not concepts:
        raise SystemExit("No concepts extracted. Check the LLM provider is reachable.")

    link_mode = bcfg.get("link_mode", "title_only")
    concepts = assign_paths(concepts)
    return cross_link(concepts, link_mode), len(docs)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an OKF bundle from raw docs.")
    parser.add_argument("--limit", type=int, default=None, help="Only process N docs.")
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    set_seed(cfg["experiment"]["seed"])

    bundle_dir = Path(cfg["paths"]["bundle"])
    results_dir = Path(cfg["paths"]["results"])
    link_mode = cfg["bundle_builder"].get("link_mode", "title_only")
    debug_dir = results_dir / "bundle_debug"
    debug_dir.mkdir(parents=True, exist_ok=True)

    all_concepts, n_docs = build_concepts(cfg, args.limit, debug_dir)
    write_bundle(all_concepts, bundle_dir)

    n_links = sum(len(c["links"]) for c in all_concepts)
    n_alias_links = sum(c.get("links_from_alias", 0) for c in all_concepts)
    okf_top_k = cfg["retrieval"]["okf"]["top_k"]
    stats = {
        "documents": n_docs,
        "concepts": len(all_concepts),
        "link_mode": link_mode,
        "cross_links": n_links,
        "links_from_alias": n_alias_links,
        "links_from_title": n_links - n_alias_links,
        "avg_links_per_concept": round(n_links / len(all_concepts), 2),
        "avg_aliases_per_concept": round(
            sum(len(c.get("aliases", [])) for c in all_concepts) / len(all_concepts), 2
        ),
        "ambiguous_aliases_detected": count_ambiguous_aliases(all_concepts, link_mode),
        "avg_body_words": round(
            sum(len(c["body"].split()) for c in all_concepts) / len(all_concepts), 1
        ),
        # How much of the bundle a single query already sees before any link
        # expansion. On a toy corpus this is large enough that expansion has
        # almost nothing left to add; on a real corpus it should be small.
        "okf_top_k": okf_top_k,
        "top_k_pct_of_bundle": round(100 * okf_top_k / len(all_concepts), 1),
    }
    results_dir.mkdir(parents=True, exist_ok=True)
    # Named per link_mode: the alias and title_only builds each keep their own
    # stats instead of the last build silently winning.
    stats_path = results_dir / f"bundle_stats_{link_mode}.json"
    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    audit_path = _write_link_audit(all_concepts, results_dir, link_mode)

    print(f"\nBundle written to {bundle_dir}")
    print(f"Stats -> {stats_path}")
    print(json.dumps(stats, indent=2))
    print(f"\nLink audit -> {audit_path}")
    print(f"  Fill the `verdict` column with correct/spurious/borderline "
          f"({n_links} links), then: python scripts/link_precision.py")
    print("\nReport these stats in the paper's dataset section.")


if __name__ == "__main__":
    main()
