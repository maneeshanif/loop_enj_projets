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
