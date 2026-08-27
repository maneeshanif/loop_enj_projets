import unittest
from calculator import sum_first_n, get_length, safe_divide

class TestCalculator(unittest.TestCase):
    def test_sum_first_5(self):
        self.assertEqual(sum_first_n(5), 15)  # 0+1+2+3+4+5 = 15

    def test_sum_first_3(self):
        self.assertEqual(sum_first_n(3), 6)  # 0+1+2+3 = 6

    def test_get_length(self):
        self.assertEqual(get_length([1, 2, 3]), 3)
        self.assertEqual(get_length([]), 0)

    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertEqual(safe_divide(-10, 2), -5)

if __name__ == '__main__':
    unittest.main()