"""Offline test of every component that does not need the embedding model or an LLM."""
import sys, json
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[1]))

from src.config import load_config, estimate_tokens, set_seed
from src.build_bundle import slugify, assign_paths, cross_link, write_bundle
from src.chunk_pipeline import chunk_text
from src.evaluate import normalise, strip_sources, parse_sources, exact_match, token_f1, retrieval_recall, citation_valid
from src.okf_pipeline import parse_links, load_bundle
from pathlib import Path

cfg = load_config(); set_seed(42)
print("config ok:", cfg["experiment"]["name"], "| budget", cfg["retrieval"]["context_token_budget"])

# --- bundle builder path assignment + cross-linking ---
concepts = [
 {"type":"Policy","title":"Attendance Requirement","description":"min attendance","tags":["attendance"],
  "body":"Students need 75 percent attendance. Those between 65 and 75 may use the Medical Exemption Process.","source_doc":"a.md"},
 {"type":"Procedure","title":"Medical Exemption Process","description":"how to apply","tags":["medical"],
  "body":"Submit Form MX-2. Approval rests with the Dean of Academics. Relates to Attendance Requirement.","source_doc":"b.md"},
 {"type":"Entity","title":"Dean of Academics","description":"the approving authority","tags":["role"],
  "body":"Sole approver of exemptions.","source_doc":"b.md"},
]
concepts = assign_paths(concepts)
print("paths:", [c["rel_path"] for c in concepts])
concepts = cross_link(concepts)
for c in concepts:
    print(" links from", c["rel_path"], "->", c["links"])
assert any(c["links"] for c in concepts), "cross-linking produced no links"

write_bundle(concepts, Path("/tmp/test_bundle"))
files = sorted(p.name for p in Path("/tmp/test_bundle").rglob("*.md"))
print("bundle files:", files)
assert "index.md" in files and "log.md" in files

# --- load it back ---
loaded = load_bundle(Path("/tmp/test_bundle"))
print("loaded concepts:", [(c.path, c.type, c.links) for c in loaded])
assert len(loaded) == 3
assert any(c.links for c in loaded), "links lost on reload"

# --- chunker ---
ch = chunk_text(" ".join(f"word{i}" for i in range(900)), 512, 64, "doc.md")
print("chunks:", len(ch), "| first id", ch[0]["id"], "| words in c0", len(ch[0]["text"].split()))
assert len(ch) >= 2

# --- metrics ---
ans = "The minimum is 75 percent.\nSOURCES: policies/attendance_requirement.md"
print("strip:", repr(strip_sources(ans)))
print("sources:", parse_sources(ans))
print("EM(75 percent):", exact_match("75 percent", "75 percent"))
print("F1:", round(token_f1(ans, "75 percent"), 3))
print("recall:", retrieval_recall("policys/attendance_requirement.md|x.md", "policys/attendance_requirement.md"))
print("citation_valid:", citation_valid(ans, "policies/attendance_requirement.md|other.md"))
print("tokens est:", estimate_tokens("a"*400))

# --- cross-linking must not nest a short title inside an existing link ---
nested = assign_paths([
 {"type":"Policy","title":"Shortfall Rule","description":"when it applies","tags":[],
  "body":"Apply via the Medical Exemption Process today.","source_doc":"a.md"},
 {"type":"Procedure","title":"Medical Exemption Process","description":"how","tags":[],
  "body":"Submit Form MX-2.","source_doc":"b.md"},
 {"type":"Definition","title":"Exemption","description":"what","tags":[],
  "body":"A waiver of a normal requirement.","source_doc":"c.md"},
])
body = cross_link(nested)[0]["body"]
print("nested-link guard:", body)
assert "[Exemption]" not in body, f"short title nested inside an existing link: {body}"
assert body.count("[") == body.count("]") == 1, f"malformed markdown links: {body}"

# --- extract_json survives the two ways gpt-oss breaks its own JSON ---
from src.llm import extract_json

bolded = '[{"type":"Fee", **description**: "a daily charge", "title":"Late Fee","body":"x"}]'
assert extract_json(bolded)[0]["description"] == "a daily charge", "bold-key repair failed"

truncated = '[{"title":"A","tags":["x","y"],"body":"first"},{"title":"B","tags":["z"],"body":"seco'
salvaged = extract_json(truncated)
print("salvaged from truncated array:", [c["title"] for c in salvaged])
assert [c["title"] for c in salvaged] == ["A"], "truncated array should keep completed objects"

# a lone object must not be mistaken for the inner array in its own tags
lone = '{"title":"A","tags":["x","y"],"body":"markdown with a [bracket] inside"}'
assert extract_json(lone)["title"] == "A", "object misparsed as its nested tags array"

# typographic characters from the generator must not zero out EM against ASCII gold
llm_answer  = "Debarred from the end‑semester examination"   # U+2011
human_gold  = "Debarred from the end-semester examination"        # ASCII hyphen
assert normalise(llm_answer) == normalise(human_gold), "unicode dash breaks normalisation"
assert exact_match(llm_answer, human_gold) == 1, "unicode dash silently zeroes EM"

# OKF blocks render as "[concept: /path]", so cited ids carry a leading slash
okf_answer = "The minimum is 75 percent.\nSOURCES: [/policies/attendance_requirement.md]"
okf_pool   = "policies/attendance_requirement.md|criteria/other.md"
assert citation_valid(okf_answer, okf_pool) == 1.0, "leading slash zeroes OKF citation_valid"

print("\nALL LOGIC TESTS PASSED")
