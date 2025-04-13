#https://github.com/rileybrubaker/lab10-RB-RK.git
#partner 1: Riley Brubaker
#partner 2: Rachel Kofman
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): 
    return a +b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def logarithm(value, base):
    if value<=0:
        raise ValueError("Logarithm underfined for non-positive values")
    if base<=0 or base==1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(value, base)

def exp(x):
    return math.exp(x)

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def square_root(x):
    if x<0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)



