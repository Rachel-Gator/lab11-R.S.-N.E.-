"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
#def add(a, b):
    #pass

import math

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



import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (a cannot be 0).")
    return b / a

def log(a, b):
    if a <= 0:
        raise ValueError("Logarithm base must be positive.")
    if a == 1:
        raise ValueError("Logarithm base cannot be 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

