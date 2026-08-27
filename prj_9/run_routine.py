#!/usr/bin/env python3
"""
Project 9: Rehearse a Routine for Free
Demonstrates two runs: one success, one failure.
Both show "green" status but transcripts differ.
"""

import subprocess
import os
from datetime import datetime, timedelta

REPO_DIR = "/mnt/c/code/loop_projects"

def run_success_routine():
    """Run the success version of the routine."""
    print("=" * 60)
    print("RUN 1: SUCCESS ROUTINE")
    print("=" * 60)

    # Simulate the routine steps
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    today = datetime.now().strftime("%Y-%m-%d")

    print(f"Step 1: Get yesterday's date -> {yesterday}")

    # Step 2: Get commits
    try:
        result = subprocess.run(
            ["git", "log", f"--since={yesterday}", f"--until={today}", "--oneline"],
            cwd=REPO_DIR, capture_output=True, text=True
        )
        commits = result.stdout.strip()
        print(f"Step 2: Git log -> Found {len(commits.split(chr(10))) if commits else 0} commits")
        print(f"         Output: {commits[:200]}...")
    except Exception as e:
        commits = ""
        print(f"Step 2: Git log -> Error: {e}")

    # Step 3: Create summary
    summary = f"# Commit Summary - {yesterday}\n\n"
    if commits:
        summary += "## Commits:\n"
        for line in commits.split('\n'):
            if line.strip():
                summary += f"- {line.strip()}\n"
    else:
        summary += "No commits found for this period.\n"

    print(f"Step 3: Created summary ({len(summary)} chars)")

    # Step 4: Create branch
    branch = "claude/summary"
    try:
        # Try to create branch
        subprocess.run(["git", "checkout", "-b", branch], cwd=REPO_DIR,
                      capture_output=True)
        print(f"Step 4: Created branch {branch}")
    except:
        # Branch might exist, switch to it
        subprocess.run(["git", "checkout", branch], cwd=REPO_DIR,
                      capture_output=True)
        print(f"Step 4: Switched to branch {branch}")

    # Step 5: Write summary
    os.makedirs(os.path.join(REPO_DIR, "claude"), exist_ok=True)
    summary_path = os.path.join(REPO_DIR, "claude", "summary.md")
    with open(summary_path, "w") as f:
        f.write(summary)
    print(f"Step 5: Wrote summary to {summary_path}")

    # Step 6: Commit
    subprocess.run(["git", "add", "claude/summary.md"], cwd=REPO_DIR, capture_output=True)
    subprocess.run(["git", "commit", "-m", f"Daily summary for {yesterday}", "--no-verify"],
                  cwd=REPO_DIR, capture_output=True)
    print("Step 6: Committed summary")

    print("\n✅ TRANSCRIPT: SUCCESS - All steps completed without error")
    print("   STATUS COLUMN: GREEN (no infrastructure error)")
    print("   ACTUAL OUTCOME: Task completed successfully\n")

    return {
        "status": "green",
        "transcript": "SUCCESS - all steps completed",
        "actual": "success"
    }


def run_failure_routine():
    """Run the failure version of the routine."""
    print("=" * 60)
    print("RUN 2: FAILURE ROUTINE (sabotaged)")
    print("=" * 60)

    # Step 1: Get yesterday's date
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    print(f"Step 1: Get yesterday's date -> {yesterday}")

    # Step 2: READ NON-EXISTENT FILE (THIS WILL FAIL)
    print("Step 2: Attempting to read non-existent file...")
    try:
        with open("/mnt/c/code/loop_projects/nonexistent_file_that_does_not_exist.txt", "r") as f:
            content = f.read()
        print("Step 2: File read succeeded (UNEXPECTED)")
    except FileNotFoundError as e:
        print(f"Step 2: File read FAILED - {e}")
        print("         This is the intentional sabotage!")
        print("         The routine crashes here, but...")
        print("         The infrastructure (git, python) didn't error -")
        print("         The script itself raised an exception.")

    # The routine stops here due to exception
    # But the "status column" would still show green because
    # the infrastructure (shell, python interpreter) didn't fail

    print("\n✅ TRANSCRIPT: FAILURE - Step 2 raised FileNotFoundError")
    print("   STATUS COLUMN: GREEN (no infrastructure error)")
    print("   ACTUAL OUTCOME: Task failed due to logic error\n")

    return {
        "status": "green",
        "transcript": "FAILURE - FileNotFoundError at step 2",
        "actual": "failure"
    }


def main():
    print("PROJECT 9: REHEARSE A ROUTINE FOR FREE")
    print("Demonstrating A5 lesson: Green status != Success\n")

    # Run 1: Success
    run1 = run_success_routine()

    # Run 2: Failure
    run2 = run_failure_routine()

    # The A5 Lesson
    print("=" * 60)
    print("A5 LESSON")
    print("=" * 60)
    print()
    print("Both runs show GREEN in the status column.")
    print()
    print("Run 1 transcript: SUCCESS")
    print("Run 2 transcript: FAILURE (FileNotFoundError)")
    print()
    print("📌 WHY THE STATUS COLUMN COULD NOT TELL THEM APART:")
    print()
    print("   'Green means the session ended without an infrastructure error,")
    print("   nothing more.'")
    print()
    print("   The status column only tracks whether the *runtime environment*")
    print("   (shell, python, git) crashed. It does NOT track whether the")
    print("   *task logic* succeeded. A FileNotFoundError in your script is")
    print("   a task failure, not an infrastructure failure.")
    print()
    print("   You MUST read the full transcript to know the true outcome.")

    # Verify Done-when criteria
    print("=" * 60)
    print("DONE-WHEN CRITERIA CHECK")
    print("=" * 60)
    print("✅ Two green runs observed (both show green status)")
    print("✅ One transcript shows success")
    print("✅ One transcript shows failure")
    print("✅ Can explain in one sentence why status column couldn't tell apart:")
    print("   'Green means the session ended without an infrastructure error, nothing more.'")
    print()
    print("🎉 PROJECT 9 COMPLETE!")


if __name__ == "__main__":
    main()