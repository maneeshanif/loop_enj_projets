import unittest

# Small failing tests - will be fixed by the loop
class TestMath(unittest.TestCase):
    def test_addition(self):
        # Initially fails - will be fixed to pass
        self.assertEqual(1 + 1, 2)  # Wrong!

    def test_subtraction(self):
        # Initially fails - will be fixed to pass
        self.assertEqual(5 - 2, 3)  # Wrong!

    def test_multiplication(self):
        # Initially fails - will be fixed to pass
        self.assertEqual(3 * 4, 12)  # Wrong!
