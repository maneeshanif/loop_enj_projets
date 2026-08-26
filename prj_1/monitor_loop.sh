#!/bin/bash
# Monitor loop that checks every minute for task completion
TASK_DONE_FILE="/mnt/c/code/loop_projects/prj_1/task_done.txt"
CHECK_INTERVAL=60  # seconds (1 minute)

echo "Starting monitor loop - checking for task completion every ${CHECK_INTERVAL} seconds..."

while true; do
    if [ -f "$TASK_DONE_FILE" ]; then
        echo "=== TASK COMPLETED ==="
        cat "$TASK_DONE_FILE"
        break
    else
        echo "[$(date '+%H:%M:%S')] Task not yet complete, waiting ${CHECK_INTERVAL}s..."
    fi
    sleep $CHECK_INTERVAL
done

echo "Monitor loop exiting cleanly."