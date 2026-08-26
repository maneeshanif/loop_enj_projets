#!/bin/bash
# Long-running task that sleeps for 120 seconds then writes a completion file
sleep 120
echo "Task completed at $(date)" > /mnt/c/code/loop_projects/prj_1/task_done.txt
echo "Long task finished"