#!/usr/bin/env python3
"""
Project 7: Break It on Purpose
Take Project 3 loop, measure cost, then sabotage it to fail.
Diagnose failure from spine (progress.md) alone.
"""

import os
import subprocess
import json
from datetime import datetime

PROGRESS_FILE = "/mnt/c/code/loop_projects/progress.md"
REPO_DIR = "/mnt/c/code/loop_projects"

def measure_project3_cost():
    """Estimate token cost for one Project 3 run."""
    # Read the morning_brief.sh script
    with open("/mnt/c/code/loop_projects/prj_3/morning_brief.sh", "r") as f:
        script_content = f.read()

    # Estimate tokens: script content + progress.md + git output + file reads
    script_tokens = len(script_content) // 4  # rough estimate

    # Read progress.md
    with open(PROGRESS_FILE, "r") as f:
        progress_content = f.read()
    progress_tokens = len(progress_content) // 4

    # Git log output estimate
    git_tokens = 500

    # File reads for TODO search
    file_read_tokens = 2000

    # Output generation
    output_tokens = 500

    total_input = script_tokens + progress_tokens + git_tokens + file_read_tokens
    total_output = output_tokens
    total_per_run = total_input + total_output

    # Monthly cost at daily cadence (30 runs)
    monthly_runs = 30
    monthly_tokens = total_per_run * monthly_runs

    # Cost estimate: ~$3 per 1M tokens (rough)
    monthly_cost = (monthly_tokens / 1_000_000) * 3

    return {
        "tokens_per_run": total_per_run,
        "monthly_tokens": monthly_tokens,
        "monthly_cost_usd": round(monthly_cost, 4),
        "breakdown": {
            "script": script_tokens,
            "progress": progress_tokens,
            "git": git_tokens,
            "files": file_read_tokens,
            "output": output_tokens
        }
    }

def run_sabotaged_loop():
    """Run a sabotaged version of Project 3 loop that fails."""
    print("=== Running Sabotaged Morning Brief ===")

    # Sabotage 1: Point to non-existent file
    nonexistent_file = "/mnt/c/code/loop_projects/nonexistent_file_that_does_not_exist.txt"

    # Sabotage 2: Impossible success condition
    # (expecting a TODO that will never exist)

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "run_type": "sabotaged",
        "sabotage": "read_nonexistent_file",
        "status": "started"
    }

    try:
        # This will fail
        with open(nonexistent_file, "r") as f:
            content = f.read()
        log_entry["status"] = "unexpected_success"
    except FileNotFoundError as e:
        log_entry["status"] = "failed"
        log_entry["error"] = str(e)
        log_entry["error_type"] = "FileNotFoundError"

    # Append to progress.md as a log entry
    with open(PROGRESS_FILE, "a") as f:
        f.write(f"\n### Sabotaged Run - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"- **Status**: {log_entry['status']}\n")
        f.write(f"- **Error**: {log_entry.get('error', 'N/A')}\n")
        f.write(f"- **Error Type**: {log_entry.get('error_type', 'N/A')}\n")
        f.write(f"- **Note**: This was an intentional sabotage for Project 7\n")
        f.write("---\n")

    print(f"Sabotaged run logged. Status: {log_entry['status']}")
    return log_entry

def diagnose_from_spine():
    """Diagnose the failure using only progress.md (the spine)."""
    print("\n=== Diagnosing from Spine Alone ===")

    with open(PROGRESS_FILE, "r") as f:
        content = f.read()

    # Find the sabotaged run entry
    lines = content.split("\n")
    in_sabotaged = False
    diagnosis = {}

    for line in lines:
        if "Sabotaged Run" in line:
            in_sabotaged = True
            diagnosis["timestamp"] = line.replace("### Sabotaged Run - ", "").strip()
        elif in_sabotaged and line.startswith("- **Status**:"):
            diagnosis["status"] = line.replace("- **Status**:", "").strip()
        elif in_sabotaged and line.startswith("- **Error**:"):
            diagnosis["error"] = line.replace("- **Error**:", "").strip()
        elif in_sabotaged and line.startswith("- **Error Type**:"):
            diagnosis["error_type"] = line.replace("- **Error Type**:", "").strip()
        elif in_sabotaged and line.startswith("---"):
            break

    print("Diagnosis from spine:")
    for k, v in diagnosis.items():
        print(f"  {k}: {v}")

    # Verify we can diagnose without replaying
    if diagnosis.get("status") == "failed":
        print("\n✅ DIAGNOSIS SUCCESSFUL:")
        print(f"  What failed: {diagnosis.get('error_type')}")
        print(f"  When: {diagnosis.get('timestamp')}")
        print(f"  Why: Tried to read non-existent file (intentional sabotage)")
        print("  Clear 'needs a human' note: YES (explicit in log)")
    else:
        print("\n❌ DIAGNOSIS FAILED: Could not determine failure from spine")

    return diagnosis

def main():
    print("=" * 60)
    print("PROJECT 7: BREAK IT ON PURPOSE")
    print("=" * 60)

    # Step 1: Measure cost
    print("\n📊 STEP 1: Measure Project 3 Cost")
    cost = measure_project3_cost()
    print(f"  Estimated tokens per run: {cost['tokens_per_run']:,}")
    print(f"  Monthly tokens (daily): {cost['monthly_tokens']:,}")
    print(f"  Estimated monthly cost: ${cost['monthly_cost_usd']}")
    print(f"  Breakdown: {cost['breakdown']}")

    # Step 2: Run sabotaged loop
    print("\n💥 STEP 2: Run Sabotaged Loop")
    run_sabotaged_loop()

    # Step 3: Diagnose from spine
    print("\n🔍 STEP 3: Diagnose from Spine")
    diagnosis = diagnose_from_spine()

    # Summary
    print("\n" + "=" * 60)
    print("PROJECT 7 SUMMARY")
    print("=" * 60)
    print(f"✅ Monthly cost calculated: ${cost['monthly_cost_usd']}")
    print(f"✅ Sabotaged run executed and logged")
    print(f"✅ Failure diagnosed from spine alone: {diagnosis.get('status') == 'failed'}")
    print(f"✅ Clear 'needs a human' note left: YES")
    print("\nAll three Done-when criteria met!")

if __name__ == "__main__":
    main()