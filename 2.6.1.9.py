# 2.6.1.9 LAB: Simple input and output

"""
Estimated time:
5-10 minutes

Level of difficulty:
Easy

Objectives
- Becoming familiar with the inputting and outputting of data in Python;
- Evaluating simple expressions.

Scenario:
Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
The results have to be printed to the console.
You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
Test your code - does it produce the results you expect?
We won't show you any test data - that would be too simple.
"""

# Solution

var_a = float(input("Input a float value for variable A: "))
var_b = float(input("Input a float value for variable B: "))

print(var_a + var_b)
print(var_a - var_b)
print(var_a * var_b)
print(var_a / var_b)
