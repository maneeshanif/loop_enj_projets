# Routine: Summarize Yesterday's Commits (Failure Version)

## Prompt
Summarize yesterday's commits onto a `claude/summary` branch.

### Steps:
1. Get yesterday's date
2. Read the file `/mnt/c/code/loop_projects/nonexistent_file_that_does_not_exist.txt` (THIS FILE DOES NOT EXIST)
3. Run `git log --since="yesterday" --until="today" --oneline` to get commits
4. Create a summary of the commits
5. Create or update branch `claude/summary`
6. Write summary to `claude/summary.md`
7. Commit and push

### Expected Output
A markdown file with commit summaries from yesterday.

### Failure Criteria
- Script MUST fail at step 2 because the file does not exist
- This demonstrates that a routine can fail while still showing "green" in status column

---
*This routine demonstrates a failing run - the task is impossible (reading non-existent file) but the infrastructure doesn't error.*