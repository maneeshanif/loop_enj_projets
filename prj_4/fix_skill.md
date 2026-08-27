---
name: fix-bug-skill
description: Skill for fixing bugs with maker-checker pattern
---

# Bug Fix Skill

## Steps for the Implementer (Maker)

1. **Analyze the bug**: Read the issue description and understand what's broken
2. **Locate the code**: Find the relevant files in the worktree
3. **Draft a fix**: Make minimal, targeted changes to fix the bug
4. **Test locally**: Run any existing tests to ensure the fix works
5. **Submit for review**: The checker will review your changes

## Reviewer (Checker) Instructions

The checker will evaluate the fix and respond with either:
- `PASS` - if the fix correctly addresses the bug without introducing new issues
- `FAIL` - if the fix is incomplete, incorrect, or introduces new problems

The checker should look for:
- Does the fix actually resolve the reported bug?
- Are there any regressions or new bugs introduced?
- Is the fix minimal and focused?
- Does it follow the project's coding standards?
