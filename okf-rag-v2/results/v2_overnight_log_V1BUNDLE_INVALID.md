> **SUPERSEDED — INVALID.** This documents the 2026-08-28 Kaggle run, which
> generated against the **v1 bundle**. Results are not v2 results. Kept for
> reference only. See `v2_SUPERSEDED_V1BUNDLE/_SUPERSEDED_README.md`.

# v2 overnight monitoring log

Started 2026-08-28 ~19:41 UTC. Autonomous monitoring per user's overnight instruction.
Push cap: 15. Fixes only applied with a named, verified root cause (see CLAUDE.md discipline).

| time (UTC) | event |
|---|---|
| 19:41 | Kernel v3 RUNNING (pushed after max_tokens 1200->4000 fix + dataset v2 with <think>-strip). Quota 2.25h/30h used. Starting 5-min poll loop. |
| 19:46 | Kernel v3 RUNNING. Smoke test in progress (chunk/full 0/3, just started -- config/qid checks all passed first). Quota 2.43h/30h. User confirmed going offline; continuing autonomous loop, no more chat until DONE/BLOCKED/cap. |
| 19:52 | Smoke test PASSED (no crash -- cell moved on). Full run started: chunk arm 16/60, ~7-9s/q. No errors. |
| 19:58 | Chunk arm COMPLETE: 60/60 rows, 0 errors, ~9 min. Starting OKF arm generation. |
| 20:04 | OKF arm 31/60, 0 errors, healthy pace. |
| 20:10 | Both generation arms COMPLETE (120 total rows implied by "scoring: /120"). No errors seen. Judging started with qwen2.5:7b-instruct, ~1-3s/row after warmup. |
| 20:16 | Kernel status COMPLETE. 120/120 raw, 120/120 scored, 60/60 per arm both stages -- notebook's own assertion cell confirmed "COMPLETE -- all 60 qids present in both arms, both stages." Total quota used this run: ~0.72h (2.25h->2.97h). Judge-label (PRELIMINARY): chunk hallucination=0.0667, okf hallucination=0.1167 -- OKF hallucinates MORE, same direction as v1. Downloading output files now for verification and wrap-up. |
| 20:35 | WRAP-UP DONE. Verified 120/120 raw+scored, 0 empty, 0 unparsed labels, qids match. Built human_labelling_sheet_v2.csv (120 rows, correcting the kernel's own 60-row sampled/judge_label-attached sheet). Wrote results/v2_overnight_summary.md and appended CLAUDE.md session log. Run is COMPLETE, not blocked. Handing off. |
