#https://github.com/rileybrubaker/lab10-RB-RK.git
#partner 1: Riley Brubaker
#partner 2: Rachel Kofman
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
         self.assertEqual(add(2, 3), 5)
         self.assertEqual(add(-1, 1), 0)
         self.assertEqual(add(0,0),0)

    def test_subtract(self): # 3 assertions
         self.assertEqual(subtract(5,3),2)
         self.assertEqual(subtract(0,-3),3)
         self.assertEqual(subtract(-2,-2),0)
         

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 4), -4)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(-9, 3), -3)
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self):
         self.assertAlmostEqual(logarithm(100,10),2)
         self.assertAlmostEqual(logarithm(8,2),3)
         self.assertAlmostEqual(logarithm(1,10),0)# 3 assertions
  

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10,-2)
        with self.assertRaises(ValueError):
            logarithm(10,1)
        

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5, 2)
    

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
