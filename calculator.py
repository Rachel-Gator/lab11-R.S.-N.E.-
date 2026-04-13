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

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
        a != 0
        if a == 0:
            raise ZeroDivisionError
        return b / a


def logarithm(a, b):
        a !=0
        b !=0
        if a == 0 or b == 0:
            raise ValueError
        return math.log(b, a)

def exponent(a, b):
    return a ** b