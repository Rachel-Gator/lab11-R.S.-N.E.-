# https://github.com/Rachel-Gator/lab11-R.S.-N.E.-
# Partner 1: Rachel Stribling
# Partner 2: Nicolas Estevez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
#def add(a, b):
    #pass

import math

def square_root(a):
    a >= 0
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (a cannot be 0).")
    return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Logarithm base must be positive.")
    if a == 1:
        raise ValueError("Logarithm base cannot be 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

