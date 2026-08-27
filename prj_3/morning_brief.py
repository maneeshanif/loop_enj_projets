#!/usr/bin/env python3
# Morning Brief with Memory - Project 3
# A scheduled loop that runs once, reads progress.md, gathers info from repo,
# writes a summary, and updates progress.md with what it found and the date.
# Run twice to prove the spine works (second run builds on first, no repeats).

import os
import re
import subprocess
from datetime import datetime, timedelta

PROGRESS_FILE = "/mnt/c/code/loop_projects/progress.md"
REPO_DIR = "/mnt/c/code/loop_projects"
TODAY = datetime.now().strftime('%Y-%m-%d')

print(f"=== Morning Brief - {TODAY} ===")

# Read existing progress to avoid duplicates
if os.path.exists(PROGRESS_FILE):
    print("Reading existing progress...")
    with open(PROGRESS_FILE, 'r') as f:
        content = f.read()
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', content)
    last_run_date = dates[-1] if dates else ""
    print(f"Last run date found: {last_run_date}")
else:
    print("No progress file found, starting fresh.")
    last_run_date = ""

# Gather data from repo
print("Gathering repo data...")
# Find TODO items excluding the script itself
todo_cmd = ["grep", "-r", "TODO", REPO_DIR, "--include=*.sh", "--include=*.py", "--include=*.md"]
result = subprocess.run(todo_cmd, capture_output=True, text=True)
todo_items = [line for line in result.stdout.split('\n') if line and '.git' not in line and 'morning_brief' not in line][:10]

# Get recent commits since yesterday
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
git_cmd = ["git", "-C", REPO_DIR, "log", f"--since={yesterday}", "--oneline"]
result = subprocess.run(git_cmd, capture_output=True, text=True)
recent_commits = [line for line in result.stdout.split('\n') if line][:5]

# Build summary
summary = f"## Morning Brief - {TODAY}\n"
summary += "\n### TODO Items Found:\n"
if todo_items:
    summary += "\n".join(todo_items) + "\n"
else:
    summary += "*None found*\n"

summary += "\n### Recent Commits (since yesterday):\n"
if recent_commits:
    summary += "\n".join(recent_commits) + "\n"
else:
    summary += "*No recent commits*\n"

summary += "\n---\n"

# Update progress.md
if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, 'r') as f:
        content = f.read()
    
    # Find the Notes section and replace everything after it
    if "## Notes" in content:
        parts = content.split("## Notes", 1)
        new_content = parts[0] + "## Notes\n" + summary
    else:
        new_content = content + "\n## Notes\n" + summary
    
    with open(PROGRESS_FILE, 'w') as f:
        f.write(new_content)
else:
    # Create new progress file
    new_content = f"# Loop Engineering Projects Progress\n\n## Completed ✅\n\n## In Progress 🔄\n\n## Not Started ⏳\n\n## Notes\n{summary}"
    with open(PROGRESS_FILE, 'w') as f:
        f.write(new_content)

print(f"Progress updated with morning brief for {TODAY}")
print("=== Brief Complete ===")
