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
