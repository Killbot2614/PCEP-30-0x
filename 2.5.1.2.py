# 2.5.1.2 LAB: Comments

"""
Estimated time:
5 minutes

Level of difficulty:
Very Easy

Objectives:
- Becoming familiar with the concept of comments in Python;
- Using and not using comments;
- Replacing comments with code;
- Experimenting with Python code.

Scenario:
The code in the editor contains comments. Try to improve it: add or remove comments where you find it appropriate (yes, sometimes removing a comment can make the code more readable), and change variable names where you think this will improve code comprehension.

Note:
Comments are very important. They are used not only to make your programs easier to understand, but also to disable those pieces of code that are currently not needed (e.g., when you need to test some parts of your code only, and ignore other). Good programmers describe each important piece of code, and give self-commenting names to variables, as sometimes it is simply much better to leave information in the code.

It's good to use readable variable names, and sometimes it's better to divide your code into named pieces (e.g., functions). In some situations, it's a good idea to write the steps of computations in a clearer way.

One more thing: it may happen that a comment contains a wrong or incorrect piece of information - you should never do that on purpose!
"""

# Solution

# This program computes the number of seconds in a given number of hours

no_of_hours = 3  # Number of hours
seconds_in_hour = 3600  # Number of seconds in 1 hour

print("Hours: ", no_of_hours)  # Printing the number of hours
print("Seconds in Hours: ", no_of_hours * seconds_in_hour) # Printing the number of seconds in a given number of hours

print("Goodbye")
