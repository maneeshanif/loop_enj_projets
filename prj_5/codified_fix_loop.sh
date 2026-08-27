#!/bin/bash
# Project 5: Codify the Body - Dynamic Workflows
# Shell script version (OpenCode approach) of the fix loop body

set -e

REPO_DIR="/mnt/c/code/loop_projects"
BASE_WORKTREE_DIR="/mnt/c/code/loop_projects/.worktrees_p5"

BUGS=(
    "bug1:off_by_one:buggy_code1.py:test_bug1.py:Fix off-by-one in loop"
    "bug2:null_check:buggy_code2.py:test_bug2.py:Add missing null check"
    "bug3:division:buggy_code3.py:test_bug3.py:Fix division by zero"
)

echo "=== Project 5: Codified Fix Loop Body ==="
echo "ENGINE (workflow body) - not a loop yet"
echo "To make it a loop: heartbeat (scheduler) + spine (progress file)"
echo ""

rm -rf "$BASE_WORKTREE_DIR"
mkdir -p "$BASE_WORKTREE_DIR"

cd "$REPO_DIR"
mkdir -p "$REPO_DIR/prj_5/bugs"

cat > "$REPO_DIR/prj_5/bugs/buggy_code1.py" << 'BUG1EOF'
def sum_first_n(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
BUG1EOF

cat > "$REPO_DIR/prj_5/bugs/test_bug1.py" << 'TEST1EOF'
import unittest
from buggy_code import sum_first_n

class TestBug1(unittest.TestCase):
    def test_sum_first_5(self):
        self.assertEqual(sum_first_n(5), 10)
    def test_sum_first_3(self):
        self.assertEqual(sum_first_n(3), 3)
    def test_sum_first_0(self):
        self.assertEqual(sum_first_n(0), 0)

if __name__ == "__main__":
    unittest.main()
TEST1EOF

cat > "$REPO_DIR/prj_5/bugs/buggy_code2.py" << 'BUG2EOF'
def get_length(items):
    return len(items)
BUG2EOF

cat > "$REPO_DIR/prj_5/bugs/test_bug2.py" << 'TEST2EOF'
import unittest
from buggy_code import get_length

class TestBug2(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(get_length([1,2,3]), 3)
    def test_empty_list(self):
        self.assertEqual(get_length([]), 0)
    def test_none_input(self):
        self.assertEqual(get_length(None), 0)

if __name__ == "__main__":
    unittest.main()
TEST2EOF

cat > "$REPO_DIR/prj_5/bugs/buggy_code3.py" << 'BUG3EOF'
def safe_divide(a, b):
    return a / b
BUG3EOF

cat > "$REPO_DIR/prj_5/bugs/test_bug3.py" << 'TEST3EOF'
import unittest
from buggy_code import safe_divide

class TestBug3(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(safe_divide(10, 2), 5)
    def test_divide_by_zero(self):
        self.assertIsNone(safe_divide(10, 0))
    def test_negative(self):
        self.assertEqual(safe_divide(-10, 2), -5)

if __name__ == "__main__":
    unittest.main()
TEST3EOF

cat > "$REPO_DIR/prj_5/fix_skill.md" << 'SKILLEOF'
---
name: fix-bug-skill-v2
description: Skill for fixing bugs with maker-checker pattern
---

# Bug Fix Skill v2

## Steps for the Implementer (Maker)
1. Analyze the bug
2. Locate the code
3. Draft a fix
4. Test locally
5. Submit for review

## Reviewer (Checker) Instructions
- PASS - fix correct, no new issues
- FAIL - incomplete, incorrect, or new problems
SKILLEOF

RESULTS=()

for bug_spec in "${BUGS[@]}"; do
    IFS=':' read -r bug_name bug_type buggy_file test_file fix_desc <<< "$bug_spec"

    echo ""
    echo "=== Processing $bug_name ($bug_type) ==="
    echo "Fix: $fix_desc"

    WORKTREE="$BASE_WORKTREE_DIR/$bug_name"
    BRANCH="fix/$bug_name"

    git branch "$BRANCH" main 2>/dev/null || git branch -f "$BRANCH" main
    git worktree add "$WORKTREE" "$BRANCH"

    cp "$REPO_DIR/prj_5/fix_skill.md" "$WORKTREE/"
    cp "$REPO_DIR/prj_5/bugs/$buggy_file" "$WORKTREE/buggy_code.py"
    cp "$REPO_DIR/prj_5/bugs/$test_file" "$WORKTREE/test_buggy.py"

    case $bug_type in
        off_by_one)
            sed -i 's/range(n + 1)/range(n)/' "$WORKTREE/buggy_code.py"
            ;;
        null_check)
            sed -i 's/return len(items)/if items is None:\n        return 0\n    return len(items)/' "$WORKTREE/buggy_code.py"
            ;;
        division)
            sed -i 's/return a \/ b/if b == 0:\n        return None\n    return a \/ b/' "$WORKTREE/buggy_code.py"
            ;;
    esac

    cd "$WORKTREE"
    if python3 test_buggy.py 2>&1 | grep -q "OK"; then
        echo "PASS - Tests pass after fix"
        RESULT="PASS"
        git add buggy_code.py
        git commit -m "Fix: $fix_desc" --no-verify
        echo "  Committed to branch: $BRANCH"
    else
        echo "FAIL - Tests still failing"
        RESULT="FAIL"
    fi

    RESULTS+=("$bug_name:$RESULT")

    cd "$REPO_DIR"
    git worktree remove "$WORKTREE" --force
done

echo ""
echo "=== SUMMARY ==="
for result in "${RESULTS[@]}"; do
    IFS=':' read -r name res <<< "$result"
    if [ "$res" = "PASS" ]; then
        echo "✓ $name: PASS - PR ready on branch fix/$name"
    else
        echo "✗ $name: FAIL - No PR"
    fi
done

echo ""
echo "=== KEY INSIGHT ==="
echo "This is the ENGINE (workflow body). Runs once on command."
echo "NO MEMORY - fresh run = fresh state."
echo ""
echo "To make this a LOOP, it needs:"
echo "1. HEARTBEAT - something that fires it (cron, event, schedule)"
echo "2. SPINE - a progress file (progress.md) that persists state"
echo ""
echo "Without these, it's just a one-shot workflow, not a loop."