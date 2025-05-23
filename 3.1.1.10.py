#  3.1.1.10 LAB: Comparison operators and conditional execution

"""
Estimated time:
5-15 minutes

Level of difficulty:
Easy

Objectives:
- Becoming familiar with the input() function;
- Becoming familiar with comparison operators in Python;
- Becoming familiar with the concept of conditional execution.

Scenario:
Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.

Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

Write a program that utilizes the concept of conditional execution, takes a string as input, and:
- Prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
- Prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
- Prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

Test Data
Sample input: spathiphyllum
Expected output: No, I want a big Spathiphyllum!

Sample input: pelargonium
Expected output: Spathiphyllum! Not pelargonium!

Sample input: Spathiphyllum
Expected output: Yes - Spathiphyllum is the best plant ever!
"""

# Solution

response = input("Type response here: ")

if response == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif response == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {response}!")
