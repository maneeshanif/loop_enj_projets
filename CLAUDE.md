# CLAUDE.md - Loop Engineering Projects Tracker

## Purpose
This file provides instructions for tracking progress across the 12 loop engineering projects in this repository.

## Instructions for Each Session

### 1. Check Project Completion Status
On session start, run this to see what's been completed:

```bash
ls -la /mnt/c/code/loop_projects/prj_*
```

Look for:
- Completed project folders with implementation files
- Any `progress.md` files inside project folders
- Test results or verification outputs

### 2. Read PROJECTS.md for Reference
Read the main projects file to understand all 12 projects:

```bash
cat /mnt/c/code/loop_projects/PROJECTS.md
```

### 3. Update Progress Tracking
Maintain a `progress.md` file in the root that tracks:

- Which projects are **completed** ✅
- Which are **in progress** 🔄
- Which are **not started** ⏳
- Key learnings from each completed project
- Any blockers or notes

### 4. Progress File Format
The `progress.md` should follow this structure:

```markdown
# Loop Engineering Projects Progress

## Completed ✅
- Project 1: In-Session Loop Monitoring — [date] — [key learning]
- Project 2: Conditional Loop — [date] — [key learning]
...

## In Progress 🔄
- Project X: [name] — [current step] — [blocker if any]

## Not Started ⏳
- Project X: [name]
...

## Notes
- [Any cross-project insights, patterns noticed, etc.]
```

### 5. When Completing a Project
After finishing a project:
1. Verify the "Done when" criteria from PROJECTS.md are met
2. **Create a new branch for the completed project:**
   ```bash
   git checkout -b project-<N>-<short-name>
   # Example: git checkout -b project-1-in-session-loop
   ```
3. **Commit all project files** (implementation, tests, docs) to this branch
4. **Push the branch to origin:**
   ```bash
   git push -u origin project-<N>-<short-name>
   ```
5. Add entry to Completed section in progress.md with date and key learning
6. Move from In Progress to Completed
7. Note any reusable patterns or code for future projects

### 6. Project Dependencies
Note the dependency chain from the course:
- Projects 1-3: Can start immediately (ready now)
- Project 4: Needs Concepts 8, 9, 11 (Part 3)
- Project 5: Needs Project 4 + dynamic workflows interlude
- Project 6: Needs Concepts 7, 10 (Part 3) — event-driven, connectors
- Project 7: Needs Project 3 + Concepts 13, 14
- Project 8 (Capstone): Needs all six parts
- Projects 9-11: Appendix drills (need Routines access)
- Project 12 (Capstone): Needs Project 3 or 8 + Concept 12 improvement loop

## Quick Commands

```bash
# View all project folders
ls -la /mnt/c/code/loop_projects/prj_*

# Check for progress.md in each project
find /mnt/c/code/loop_projects/prj_* -name "progress.md" -exec echo "=== {} ===" \; -exec cat {} \;

# Quick status overview
cat /mnt/c/code/loop_projects/progress.md 2>/dev/null || echo "No root progress.md yet"
```

## Reminder
- Use throwaway git repos for each project (don't risk real work)
- Set limits first (max tries, max minutes, max spend) — Concept 13
- Prove loops watched before unattended — Part 6 rule
- The spine (progress.md) is what makes it a loop, not a one-off — Concept 12