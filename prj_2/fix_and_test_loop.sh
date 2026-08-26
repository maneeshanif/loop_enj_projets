#!/bin/bash
# Loop that keeps fixing tests and running them until they pass (max 6 tries)
MAX_TRIES=6
TRY=0

echo "Starting fix-and-test loop (max $MAX_TRIES tries)..."

while [ $TRY -lt $MAX_TRIES ]; do
    TRY=$((TRY + 1))
    echo ""
    echo "=== Try $TRY / $MAX_TRIES ==="

    # Run the test runner - IT decides if tests pass
    if python3 run_tests.py; then
        echo ""
        echo "✓ Tests passed! Loop stopping because tests actually passed."
        exit 0
    else
        echo "✗ Tests failed. Fixing..."

        # Fix one test per iteration (maker) - use Python for precise editing
        export TRY_NUM=$TRY
        python3 -c "
import sys
import os

try_num = int(os.environ.get('TRY_NUM', '0'))
with open('test_failing.py', 'r') as f:
    content = f.read()

if try_num == 1:
    content = content.replace('assertEqual(1 + 1, 3)', 'assertEqual(1 + 1, 2)')
    print('  Fixed test_addition')
elif try_num == 2:
    content = content.replace('assertEqual(5 - 2, 2)', 'assertEqual(5 - 2, 3)')
    print('  Fixed test_subtraction')
elif try_num == 3:
    content = content.replace('assertEqual(3 * 4, 11)', 'assertEqual(3 * 4, 12)')
    print('  Fixed test_multiplication')

with open('test_failing.py', 'w') as f:
    f.write(content)
"
    fi
done

echo ""
echo "✗ Hit max tries ($MAX_TRIES) without tests passing."
echo "  Stop condition or fix logic needs work."
exit 1
