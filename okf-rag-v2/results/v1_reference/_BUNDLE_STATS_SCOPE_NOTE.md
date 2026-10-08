# Scope note: what the bundle_stats files here describe (2026-08-28)

`okf_bundle_stats.json` and `okf_bundle_title_only_stats.json` in this directory
describe **v1's bundle**, which still exists and is unchanged at
`PUBLICATION_v1/bundle/okf_bundle/`. They are valid, current v1 evidence and are
NOT stale.

They were considered for archiving when `data/okf_bundle/` was cleared, and
deliberately left in place: `results/v1_reference/` is frozen v1 evidence
(read-only by project rule), `scripts/link_precision.py` reads the stats file by
path, and the graded link-precision numbers inside (strict 0.44 / lenient 0.79,
alias 0.315 / title 0.778) are cited in the paper's limitations section.

**They describe no v2 bundle.** When v2's Nemotron bundle is built it writes its
own `bundle_stats_<link_mode>.json` under `results/`. Do not compare these
numbers to a v2 bundle without saying which bundle each came from.
