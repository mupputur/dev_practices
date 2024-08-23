import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5,12),7)


    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-10,20),-30)


    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-10,9),-90)


    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(50, -5), -10)

        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == '__main__':
    unittest.main()
