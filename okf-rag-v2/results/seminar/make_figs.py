"""Figures for the PIET seminar report. Every number is read from a result file
or transcribed from one; nothing here is invented."""
import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp

R = "../"
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
                     "font.size": 10, "axes.grid": True, "grid.alpha": .3,
                     "axes.axisbelow": True, "figure.dpi": 200})
CH, OK = "#4C72B0", "#C44E52"

# ---- Fig 3.2: hallucination rate, both configurations (human labels) ----
# v1: results/v1_reference/table_main_HUMAN.csv ; v2: results/v2_kaggle/table_main_human.csv
fig, ax = plt.subplots(figsize=(5.4, 3.2))
x = [0, 1]; w = .34
ax.bar([i - w/2 for i in x], [0.0333, 0.0308], w, label="Chunk baseline", color=CH)
ax.bar([i + w/2 for i in x], [0.0833, 0.0154], w, label="OKF-RAG", color=OK)
for i, (a, b) in enumerate([(0.0333, 0.0833), (0.0308, 0.0154)]):
    ax.text(i - w/2, a + .002, f"{a:.4f}", ha="center", fontsize=8)
    ax.text(i + w/2, b + .002, f"{b:.4f}", ha="center", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(["Configuration v1\n(Llama 3.1 8B, n=60)\np = 0.31",
                                      "Configuration v2\n(Nemotron 30B, n=65)\np = 0.60"])
ax.set_ylabel("Hallucination rate (human labels)")
ax.set_ylim(0, .105); ax.legend(frameon=False, fontsize=9)
ax.set_title("Neither difference is statistically significant", fontsize=9.5)
fig.tight_layout(); fig.savefig("fig/fig_hallucination.png"); plt.close(fig)

# ---- Fig 3.3: context tokens per question ----
fig, ax = plt.subplots(figsize=(5.4, 3.0))
ax.bar([i - w/2 for i in x], [1615.4, 1644.5], w, label="Chunk baseline", color=CH)
ax.bar([i + w/2 for i in x], [1162.6, 1472.8], w, label="OKF-RAG", color=OK)
for i, (a, b, d) in enumerate([(1615.4, 1162.6, "-28.0%"), (1644.5, 1472.8, "-10.4%")]):
    ax.text(i - w/2, a + 25, f"{a:.0f}", ha="center", fontsize=8)
    ax.text(i + w/2, b + 25, f"{b:.0f}", ha="center", fontsize=8)
    ax.text(i + w/2, b/2, d, ha="center", fontsize=9, color="white", weight="bold")
ax.set_xticks(x); ax.set_xticklabels(["Configuration v1", "Configuration v2"])
ax.set_ylabel("Mean retrieval context (tokens/question)")
ax.set_ylim(0, 1950); ax.legend(frameon=False, fontsize=9)
fig.tight_layout(); fig.savefig("fig/fig_tokens.png"); plt.close(fig)

# ---- Fig 3.4: link precision by match type ----
s = json.load(open(R + "v1_reference/okf_bundle_stats.json"))["link_precision"]
labs = ["All links\n(n=100)", "Title match\n(n=27)", "Alias match\n(n=73)"]
st = [s["precision_strict"], s["by_match_type"]["title"]["precision_strict"],
      s["by_match_type"]["alias"]["precision_strict"]]
le = [s["precision_lenient"], s["by_match_type"]["title"]["precision_lenient"],
      s["by_match_type"]["alias"]["precision_lenient"]]
fig, ax = plt.subplots(figsize=(5.4, 3.0))
xx = range(3)
ax.bar([i - w/2 for i in xx], st, w, label="Strict precision", color="#55A868")
ax.bar([i + w/2 for i in xx], le, w, label="Lenient precision", color="#8172B2")
for i in xx:
    ax.text(i - w/2, st[i] + .015, f"{st[i]:.3f}", ha="center", fontsize=8)
    ax.text(i + w/2, le[i] + .015, f"{le[i]:.3f}", ha="center", fontsize=8)
ax.set_xticks(list(xx)); ax.set_xticklabels(labs)
ax.set_ylabel("Precision"); ax.set_ylim(0, 1.12); ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout(); fig.savefig("fig/fig_linkprec.png"); plt.close(fig)

# ---- Fig 3.5: v2 behaviour split by question type ----
fig, ax = plt.subplots(figsize=(5.8, 3.0))
cats = ["single\n(n=37)", "multi\n(n=18)", "unanswerable\n(n=10)"]
ch_h = [0.027, 0.0556, 0.0]; ok_h = [0.0, 0.0556, 0.0]
ch_a = [0.027, 0.3889, 1.0];  ok_a = [0.0541, 0.2778, 1.0]
xx = range(3)
ax.bar([i - .27 for i in xx], ch_h, .18, label="Chunk hallucination", color=CH)
ax.bar([i - .09 for i in xx], ok_h, .18, label="OKF hallucination", color=OK)
ax.bar([i + .09 for i in xx], ch_a, .18, label="Chunk abstention", color=CH, alpha=.45, hatch="//")
ax.bar([i + .27 for i in xx], ok_a, .18, label="OKF abstention", color=OK, alpha=.45, hatch="//")
ax.set_xticks(list(xx)); ax.set_xticklabels(cats)
ax.set_ylabel("Rate"); ax.set_ylim(0, 1.18)
ax.legend(frameon=False, fontsize=7.5, ncol=2)
fig.tight_layout(); fig.savefig("fig/fig_hop.png"); plt.close(fig)

# ---- Fig 3.1: pipeline diagram ----
fig, ax = plt.subplots(figsize=(6.4, 3.6)); ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(0, 6)
def box(x, y, w_, h_, t, fc):
    ax.add_patch(mp.FancyBboxPatch((x, y), w_, h_, boxstyle="round,pad=0.08",
                                   fc=fc, ec="#333", lw=.9))
    ax.text(x + w_/2, y + h_/2, t, ha="center", va="center", fontsize=8)
def arr(x1, y1, x2, y2):
    ax.annotate("", (x2, y2), (x1, y1), arrowprops=dict(arrowstyle="->", lw=1.1, color="#333"))
box(0.2, 2.5, 1.7, 1.0, "40 Kubernetes\ndocs\n(30,102 words)", "#EEE")
box(2.5, 4.2, 2.2, 1.0, "Fixed-size chunker\n512 tok / 64 overlap", "#DCE6F2")
box(2.5, 0.8, 2.2, 1.0, "LLM concept extraction\n+ deterministic linking", "#F6DEDE")
box(5.3, 4.2, 1.9, 1.0, "Arm A\nchunk index", "#DCE6F2")
box(5.3, 0.8, 1.9, 1.0, "Arm B\nOKF bundle\n358 units / 1,031 links", "#F6DEDE")
box(7.8, 2.5, 2.0, 1.0, "Shared generator\n+ 1,800-token\ncontext budget", "#E8F0E4")
box(5.3, 2.5, 1.9, 0.85, "65 questions\n(37/18/10)", "#FFF3D0")
arr(1.9, 3.3, 2.5, 4.6); arr(1.9, 2.7, 2.5, 1.3)
arr(4.7, 4.7, 5.3, 4.7); arr(4.7, 1.3, 5.3, 1.3)
arr(7.2, 4.7, 8.8, 3.5); arr(7.2, 1.3, 8.8, 2.5); arr(7.2, 2.9, 7.8, 3.0)
fig.tight_layout(); fig.savefig("fig/fig_pipeline.png"); plt.close(fig)
print("figures written")
