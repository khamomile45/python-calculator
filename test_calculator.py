import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add(self):
        self.assertEqual(self.calc.add(-2,-5),-7)

    def test_add(self):
        self.assertEqual(self.calc.add(-2,5),3)
    
    def test_add(self):
        self.assertEqual(self.calc.add(2,-5),-3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4,-2),6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-4,-4),0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,-2),-8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-4,-2),8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,2),8)


    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2), 5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,-2), -5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(0,0), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(-10,-20), 2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(-10,-2), 5)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10,3), 3)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,5), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,3), 1)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(1,10), 1)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()