#!/usr/bin/env python3
"""
Project 6: The Doorbell Loop - PR Reviewer
Event-driven loop that reviews PRs for planted bugs.
"""

import os
import json
import subprocess
import sys

def get_pr_diff(pr_number):
    result = subprocess.run(
        ['gh', 'api', f'repos/maneeshanif/loop_enj_projets/pulls/{pr_number}/files'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error fetching PR files: {result.stderr}")
        return []
    return json.loads(result.stdout)

def analyze_diff_for_bugs(files):
    findings = []
    for file_info in files:
        filename = file_info.get("filename", "")
        patch = file_info.get("patch", "")
        if not patch:
            continue
        if "range(" in patch:
            lines = patch.split("\n")
            for i, line in enumerate(lines):
                if line.startswith("+") and "range(" in line and ("+ 1" in line or "- 1" in line):
                    findings.append({
                        "file": filename,
                        "line": i,
                        "type": "off_by_one",
                        "message": f"Possible off-by-one error in range(): {line.strip()}"
                    })
        if "is None" in patch or "is not None" in patch:
            lines = patch.split("\n")
            for i, line in enumerate(lines):
                if line.startswith("-") and ("is None" in line or "is not None" in line):
                    findings.append({
                        "file": filename,
                        "line": i,
                        "type": "removed_null_check",
                        "message": f"Null check removed: {line.strip()}"
                    })
        if "/" in patch:
            lines = patch.split("\n")
            for i, line in enumerate(lines):
                if line.startswith("+") and "/" in line and "return" in line:
                    findings.append({
                        "file": filename,
                        "line": i,
                        "type": "division_by_zero_risk",
                        "message": f"Potential division by zero: {line.strip()}"
                    })
    return findings

def post_review_comment(pr_number, findings):
    if not findings:
        body = "✅ **Doorbell Loop Review**: No obvious bug patterns detected in this PR."
    else:
        body = "🔍 **Doorbell Loop Review - Potential Issues Found**:\n\n"
        for f in findings:
            body += f"- **{f['type']}** in `{f['file']}`: {f['message']}\n"
        body += "\n*This review was generated automatically by the Doorbell Loop (Project 6).*"
    subprocess.run([
        "gh", "api", "--method", "POST",
        f"repos/maneeshanif/loop_enj_projets/issues/{pr_number}/comments",
        "-f", f"body={body}"
    ])

def main():
    pr_number = os.environ.get("PR_NUMBER")
    if not pr_number:
        print("PR_NUMBER not set")
        sys.exit(1)
    print(f"Reviewing PR #{pr_number}...")
    files = get_pr_diff(pr_number)
    findings = analyze_diff_for_bugs(files)
    post_review_comment(pr_number, findings)
    print(f"Review complete. Found {len(findings)} potential issues.")

if __name__ == "__main__":
    main()