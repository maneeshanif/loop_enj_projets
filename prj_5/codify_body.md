# Project 5: Codify the Body - Dynamic Workflows

## Concept
Take the fix loop from Project 4 and codify its body as a dynamic workflow.
The workflow should:
1. Draft fixes for multiple issues in parallel worktrees
2. Have a reviewer grade each one
3. Only open PRs for PASS grades

## Plain English Description (for dynamic workflow generation)

"Create a workflow that:
1. Takes a list of bug descriptions (each with a test file and buggy code file)
2. For each bug, creates an isolated worktree/branch
3. In each worktree, runs the tests to confirm they fail
4. Applies fixes per the fix_skill.md steps
5. Re-runs tests to verify fixes work
6. Has a reviewer agent check each fix (PASS/FAIL)
7. For PASS: commits and pushes a branch ready for PR
8. For FAIL: logs reasons and does not create PR
9. Reports summary of all results"

## Implementation Approach (Shell Script Version - OpenCode style)

Since dynamic workflows are a research preview, I'll implement both:
1. A shell script version that demonstrates the codified body
2. Documentation of what the dynamic workflow version would look like

The key insight from the interlude: a workflow is an engine, not a loop. 
To make it a loop, it needs:
- A heartbeat to fire it (schedule, event, etc.)
- A progress file (spine) that agents write to

## Done When Criteria
1. One command runs the whole draft-and-review body (multiple candidates, isolated checkouts, verdicts)
2. Proved the engine warning: fresh session remembers nothing from last run
3. Named the two things needed to become a loop: heartbeat + progress file
