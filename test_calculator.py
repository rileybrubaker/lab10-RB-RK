#https://github.com/rileybrubaker/lab10-RB-RK.git
#partner 1: Riley Brubaker
#partner 2: Rachel Kofman
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
     def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 4,) -4)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(-9, 3), -3)
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5, 2)
    

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(ypotenuse(5, 12), 13)
        self.assertAlmostEqual(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(4), 2)
        aelf.assertAlmostEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
