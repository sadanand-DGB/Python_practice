import unittest

from calculator import add, multiply


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)


if __name__ == "__main__":
    unittest.main()