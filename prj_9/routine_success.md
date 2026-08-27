# Routine: Summarize Yesterday's Commits (Success Version)

## Prompt
Summarize yesterday's commits onto a `claude/summary` branch.

### Steps:
1. Get yesterday's date
2. Run `git log --since="yesterday" --until="today" --oneline` to get commits
3. Create a summary of the commits
4. Create or update branch `claude/summary`
5. Write summary to `claude/summary.md`
6. Commit and push

### Expected Output
A markdown file with commit summaries from yesterday.

### Success Criteria
- Script runs without errors
- Summary file created with commit information
- Branch created/updated successfully

---
*This routine demonstrates a successful run - the task is achievable and completes cleanly.*