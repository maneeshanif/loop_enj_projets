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
