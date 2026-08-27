#!/usr/bin/env python3
# Tests for the buggy code - these should fail initially

import unittest
import sys
sys.path.insert(0, '.')
from buggy_code import calculate_average, find_max, is_even

class TestBuggyCode(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([10, 20, 30, 40, 50]), 30)
        self.assertEqual(calculate_average([1, 2, 3]), 2)
        self.assertEqual(calculate_average([]), 0)
    
    def test_find_max(self):
        self.assertEqual(find_max([10, 20, 30, 40, 50]), 50)
        self.assertEqual(find_max([5, 1, 9, 3]), 9)
        self.assertIsNone(find_max([]))
    
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))
        self.assertFalse(is_even(5))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-1))

if __name__ == "__main__":
    unittest.main()
