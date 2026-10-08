# ARCHIVED — this is v1's bundle, not a v2 bundle

Moved here from `data/okf_bundle/` on 2026-08-28 by user decision (Option B:
clear the v1-copied bundle, rebuild fresh with Nemotron).

**What this is:** all 371 concept files are byte-for-byte identical to
`PUBLICATION_v1/bundle/okf_bundle/` — verified by SHA-256 over the sorted tree
(`99a2242e73cb91a64a39c9bb3fbfe9f2d34fa9bf3b42f6f62faae6524f70b956`, identical
on both sides; 371/371 files match). It was produced by v1's local Ollama
`llama3.1:8b` extraction, NOT by any v2 process.

**Do not use it for v2.** v2 rebuilds its own bundle with Nemotron into
`data/okf_bundle/`. Any v2 result computed against these files is invalid —
see `results/v2_SUPERSEDED_V1BUNDLE/`.

**Not deleted** because the standing instruction was archive-only. It is fully
redundant: `PUBLICATION_v1/bundle/okf_bundle/` holds the verified-identical
copy. Safe to delete outright whenever you want.
