import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-2, -3), 1)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(0, 9), 0)
        self.assertEqual(mul(-3, 3), -9)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5,15), 3)
        self.assertEqual(div(7, -21), -3)
        self.assertEqual(div(-4, 12), -3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(5, 25), 2)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(2, 0)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(6, 7), 9.219544457)
        self.assertAlmostEqual(hypotenuse(4, 3), 5)
        self.assertAlmostEqual(hypotenuse(8, 8), 11.3137085)

    def test_sqrt(self): # 3 assertions

        with self.assertRaises(ValueError):
            square_root(-25)
        with self.assertRaises(ValueError):
            square_root(-9)
        with self.assertRaises(ValueError):
            square_root(-27)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

