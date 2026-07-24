"""Test OKF link-expansion + budget assembly with a stubbed embedding index."""
import sys, types
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[1]))

# Stub DenseIndex so we can test retrieval logic with no model download.
import src.embeddings as emb
class FakeIndex:
    """Keyword-overlap stand-in for the dense index, so ranking is meaningful."""
    def __init__(self, texts, model, bs): self.texts = list(texts)
    def search(self, q, top_k, allowed=None):
        pool = range(len(self.texts)) if allowed is None else allowed
        qw = set(q.lower().split())
        scored = [(i, len(qw & set(self.texts[i].lower().split()))) for i in pool]
        scored.sort(key=lambda x: -x[1])
        return [(i, float(s)) for i, s in scored[:top_k]]
emb.DenseIndex = FakeIndex
import src.okf_pipeline as okfp
okfp.DenseIndex = FakeIndex

from src.config import load_config
from src.build_bundle import assign_paths, cross_link, write_bundle
from pathlib import Path

concepts = [
 {"type":"Policy","title":"Attendance Requirement","description":"d","tags":[],
  "body":"Need 75 percent. See Medical Exemption Process for relief.","source_doc":"a.md"},
 {"type":"Procedure","title":"Medical Exemption Process","description":"d","tags":[],
  "body":"Form MX-2, approved by the Dean of Academics only.","source_doc":"b.md"},
 {"type":"Entity","title":"Dean of Academics","description":"d","tags":[],
  "body":"Sole approving authority for exemptions.","source_doc":"b.md"},
 {"type":"Policy","title":"Late Fee","description":"d","tags":[],
  "body":"500 rupees per day, capped at 5000.","source_doc":"a.md"},
]
write_bundle(cross_link(assign_paths(concepts)), Path("/tmp/tb2"))
print("folders:", sorted({p.parent.name for p in Path('/tmp/tb2').rglob('*.md')}))

cfg = load_config()
cfg["paths"]["bundle"] = "/tmp/tb2"

r_full = okfp.OKFRag(cfg, {"top_k":1, "hop_expansion":1, "max_expanded":4})
out = r_full.retrieve("attendance")
print("\nWITH expansion  -> units", out["n_units"], "seed", out["n_seed"], "expanded", out["n_expanded"])
print("  ids:", out["retrieved_ids"])

r_none = okfp.OKFRag(cfg, {"top_k":1, "hop_expansion":0, "max_expanded":4})
out2 = r_none.retrieve("attendance")
print("NO expansion    -> units", out2["n_units"], "expanded", out2["n_expanded"])
print("  ids:", out2["retrieved_ids"])

assert out["n_expanded"] > 0, "expansion did nothing"
assert out2["n_expanded"] == 0, "ablation switch broken"

# budget enforcement
cfg["retrieval"]["context_token_budget"] = 30
r_tight = okfp.OKFRag(cfg, {"top_k":4, "hop_expansion":1, "max_expanded":4})
out3 = r_tight.retrieve("attendance")
print("\nTIGHT budget(30)-> units", out3["n_units"], "tokens", out3["context_tokens"])
assert out3["context_tokens"] <= 30, "budget not enforced"

# two-hop reach
cfg["retrieval"]["context_token_budget"] = 1800
r2 = okfp.OKFRag(cfg, {"top_k":1, "hop_expansion":2, "max_expanded":8})
out4 = r2.retrieve("attendance")
print("TWO-hop         -> ids:", out4["retrieved_ids"])
assert len(out4["retrieved_ids"]) >= len(out["retrieved_ids"])

print("\nEXPANSION + BUDGET + ABLATION TESTS PASSED")
