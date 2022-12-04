import unittest
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(Calculator.sub(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(Calculator.mul(2, 2), 4)

    def test_divide(self):
        self.assertEqual(Calculator.div(4, 2), 2)

if __name__ == '__main__':
    unittest.main()