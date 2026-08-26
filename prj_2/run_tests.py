#!/usr/bin/env python3
# Test runner using unittest (built-in) - returns exit code 0 if all pass, non-zero if any fail
import sys
import unittest

# Import the test module
import test_failing

if __name__ == "__main__":
    # Run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_failing)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)