# Loop Engineering Projects Progress

*Last updated: 2026-08-27*

## Completed ✅
- Project 1: In-Session Loop Monitoring — 2026-08-26 — Built a monitor loop that checks every minute for a long-running task completion, notifies once when done, and exits cleanly
- Project 2: Conditional Loop: Make Tests Pass Then Stop — 2026-08-26 — Built a conditional loop that fixes failing tests one by one until all pass (stopped on try 4 of 6), using the test runner as the decision maker
- Project 3: The Morning Brief with Memory — 2026-08-27 — Built a scheduled loop that reads progress.md, gathers repo data, writes summary, and updates progress.md. Second run built on first (found previous entries as TODO), proving the spine/memory works.
- Project 4: Fix Loop with Real Checker — 2026-08-27 — Built a maker-checker loop using worktree isolation. Good fix gets PASS and PR; deliberately bad fix (divide by 999) gets FAIL with reasons. Checker correctly rejects bad fixes.
- Project 5: Codify the Body (Dynamic workflows) — 2026-08-27 — Built a dynamic workflow engine that processes 3 bugs in parallel worktrees, applies fixes via sed, runs tests as checker. All 3 pass (off-by-one, null check, division by zero). Demonstrates ENGINE vs LOOP: runs once on command, no memory between runs. To make it a loop needs heartbeat + spine.
- Project 6: The Doorbell Loop (Event-driven) — 2026-08-27 — Built a GitHub Actions workflow that triggers on PR events (opened, synchronize, reopened). Python script analyzes PR diffs for bug patterns (off-by-one, removed null checks, division by zero) and posts review comments. Completes all four heartbeats: in-session, conditional, scheduled, event-driven.
- Project 7: Break It on Purpose (Observability) — 2026-08-27 — Measured Project 3 loop cost (~$0.38/month at daily cadence). Sabotaged loop by reading non-existent file, logged failure to progress.md. Diagnosed failure from spine alone: FileNotFoundError at 2026-08-27 22:38. Clear 'needs a human' note left. All three Done-when criteria met.
- Project 8: Your Own Daily Loop — Capstone (all six parts) — 2026-08-27 — Built full daily dependency audit loop with all components: heartbeat (scheduled trigger), worktree isolation, skill (audit prompt), maker-checker pattern, connector (GitHub PR creation), spine (progress.md + loop_state.json), budget guards (Concept 13: token limits, monthly cost cap, circuit breaker).
- Project 9: Rehearse a Routine for Free (Appendix A1, A3, A5) — 2026-08-27 — Demonstrated A5 lesson: two green runs (one success, one failure with FileNotFoundError). Both show GREEN status column. One-sentence explanation: "Green means the session ended without an infrastructure error, nothing more." Status column tracks infrastructure, not task logic success.
- Project 10: The Secrets Drill (Appendix A4, A2) — 2026-08-27 — Demonstrated mechanical difference: .env file (gitignored) works locally but FAILS in cloud (fresh clone has no .env). Environment variables injected by platform SUCCEED in cloud. Key insight: "gitignored files never reach GitHub, so the fresh cloud clone never contains them."
- Project 11: Build the Two-Routine Gate (Appendix A3, A4, A6) — 2026-08-27 — Built human gate pattern: Routine A (scheduled drafter) creates reviewable draft on claude/ branch; Routine B (API-triggered approver) fires only with bearer token. A6 checklist verified: connectors pruned, unrestricted pushes off, state file chosen (gate_state.json), bearer token stored securely.

## In Progress 🔄
*None currently*

## Not Started ⏳
- Project 12: Build a Dreaming Loop — Capstone (Concepts 12, 11, 6, Part 5)

## Notes
- Projects 1-3 are "ready now" per the course (don't need later concepts)
- Project 4+ require Part 3 concepts (worktrees, skills, maker-checker)
- Project 6 requires Part 3 (event-driven, connectors)
- Project 8 & 12 are capstones requiring full course completion
- Projects 9-11 are appendix drills needing Routines access
- Project 3 verified: second run found first run's entries as TODO items, confirming memory works
- Project 4 verified: checker correctly passes good fixes and rejects bad fixes

### Sabotaged Run - 2026-08-27 22:38
- **Status**: failed
- **Error**: [Errno 2] No such file or directory: '/mnt/c/code/loop_projects/nonexistent_file_that_does_not_exist.txt'
- **Error Type**: FileNotFoundError
- **Note**: This was an intentional sabotage for Project 7
---
