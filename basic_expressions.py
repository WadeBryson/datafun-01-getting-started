"""
Purpose: Illustrate basic expresssions and operators in Python.

Author: Wade Bryson

This file name is:   basic_expressions.py
This module name is: basic_expressions

Expressions

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, or Excel expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.
 
"""

from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)

# Declare some variables 
# TODO: Try changing the values of these variables
# TODO: Add some new variables and calculate the area of a rectangle ()
triangle_base = 20
triangle_height = 3
i = 41
j = 12
a = 5.4
b = 3.5
rectangle_base = 15
rectangle_height = 10

# Try some operators (multiply, divide, add, subtract)
triangle_area = triangle_base * triangle_height / 2
sum = a + b
difference = i - j
rectangle_area = rectangle_base*rectangle_height

# Log some information using f-strings (formatted strings)
logger.info(f"Given base={triangle_base} and height={triangle_height}, the triangle area = {triangle_area}")
logger.info(f"Given a={a} and b={b}, the sum = {sum}")
logger.info(f"Given i={i} and j={j}, the difference = {difference}")
logger.info(f"Given base={rectangle_base} and height={rectangle_height}, the rectangle area = {rectangle_area}")


# Use built-in open() function to read the log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
