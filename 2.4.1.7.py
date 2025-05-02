# 2.4.1.7 LAB: Variables

"""
Estimated time:
10 minutes

Level of difficulty:
Easy

Objectives:
- Becoming familiar with the concept of storing and working with different data types in Python;
- Experimenting with Python code.

Scenario:
Here is a short story:
Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

Your task is to:
- Create the variables: john, mary, and adam;
- Assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
- Having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
- Now create a new variable named total_apples equal to addition of the three former variables.
- Print the value stored in total_apples to the console;
- Experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
"""

# Solution

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=", ")

total_apples = john + mary + adam
print("Total number of Apples: ", total_apples)
