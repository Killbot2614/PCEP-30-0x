# 2.1.1.6 LAB: The print() function

"""
Estimated Time: 5-10 minutes
Level of Difficulty: Very easy

Objectives:
- Become familiar with the print() function and its formatting capabilities.
- Experiment with Python code.

Scenario:
The print() command, which is one of the easiest directives in Python, simply prints out a line to the screen.

In this lab, you will:
1. Use the print() function to print the line "Hello, Python!" to the screen.
2. Print your first name using the print() function.
3. Remove the double quotes and run your code to observe the error thrown.
4. Remove the parentheses, put back the double quotes, and run your code again to observe the error thrown.
5. Experiment with different variations of the print() function.
"""

# Solution

# 1. Print a greeting message
print("Hello, Python!")

# 2. Print your name
print("Killbot")

# 3. Demonstrating NameError by removing quotes
# Uncomment the line below to see the error
# print(Killbot)  # This will raise a NameError

# 4. Demonstrating SyntaxError by removing parentheses
# Uncomment the line below to see the error
# print "Hello, Python!"  # This will raise a SyntaxError

# 5. Experimentation
print('Single quotes work too!')
print("Multiple print statements on the same line:", end=' ')
print("This is possible!")
