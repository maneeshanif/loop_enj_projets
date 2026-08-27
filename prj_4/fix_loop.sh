#!/bin/bash
# Fix Loop with Real Checker - Project 4
# Uses: Concept 8 (worktree), Concept 9 (skill), Concept 11 (maker-checker)

set -e

REPO_DIR="/mnt/c/code/loop_projects"
WORKTREE_DIR="/mnt/c/code/loop_projects/.worktree_fix"

echo "=== Fix Loop with Real Checker (Project 4) ==="

# Clean up
if [ -d "$WORKTREE_DIR" ]; then
    rm -rf "$WORKTREE_DIR"
fi

# Create worktree
cd "$REPO_DIR"
git branch fix-worktree-branch main 2>/dev/null || git branch -f fix-worktree-branch main
git worktree add "$WORKTREE_DIR" fix-worktree-branch

# Copy files
cp "$REPO_DIR/prj_4/fix_skill.md" "$WORKTREE_DIR/"
cp "$REPO_DIR/prj_4/buggy_code.py" "$WORKTREE_DIR/"
cp "$REPO_DIR/prj_4/test_buggy.py" "$WORKTREE_DIR/"

echo "=== Step 1: Run tests (should fail) ==="
cd "$WORKTREE_DIR"
python3 test_buggy.py || true

echo "=== Step 2: MAKER - Apply fixes ==="
sed -i 's/return total \/ (count + 1)/return total \/ count/' buggy_code.py
sed -i 's/return n % 2 == 1/return n % 2 == 0/' buggy_code.py

echo "=== Step 3: CHECKER - Review fix ==="
cd "$WORKTREE_DIR"
if python3 test_buggy.py 2>&1 | grep -q "OK"; then
    echo "PASS - All tests pass"
    CHECK_RESULT="PASS"
else
    echo "FAIL - Tests failing"
    CHECK_RESULT="FAIL"
fi

echo "=== Checker Result: $CHECK_RESULT ==="

if [ "$CHECK_RESULT" = "PASS" ]; then
    cd "$WORKTREE_DIR"
    git checkout -b fix/bug-calculations
    git add buggy_code.py
    git commit -m "Fix: calculate_average division and is_even logic"
    echo "PR from branch: fix/bug-calculations"
    git diff main -- buggy_code.py
fi

# Test bad fix
echo "=== Step 4: Test BAD fix ==="
BAD_WORKTREE="/mnt/c/code/loop_projects/.worktree_bad"
rm -rf "$BAD_WORKTREE"
git branch bad-fix-test main 2>/dev/null || git branch -f bad-fix-test main
git worktree add "$BAD_WORKTREE" bad-fix-test
cp "$REPO_DIR/prj_4/buggy_code.py" "$BAD_WORKTREE/"
cp "$REPO_DIR/prj_4/test_buggy.py" "$BAD_WORKTREE/"

cd "$BAD_WORKTREE"
sed -i 's/return total \/ (count + 1)/return total \/ 999/' buggy_code.py
echo "Applied bad fix"
python3 test_buggy.py || true

if python3 test_buggy.py 2>&1 | grep -q "OK"; then
    echo "ERROR: Bad fix passed!"
else
    echo "CORRECT: Bad fix got FAIL"
fi

# Cleanup
cd "$REPO_DIR"
git worktree remove "$WORKTREE_DIR" --force 2>/dev/null || true
rm -rf "$WORKTREE_DIR"
git worktree remove "$BAD_WORKTREE" --force 2>/dev/null || true
rm -rf "$BAD_WORKTREE"
git branch -D fix-worktree-branch 2>/dev/null || true
git branch -D bad-fix-test 2>/dev/null || true
echo "=== Project 4 Complete ==="
