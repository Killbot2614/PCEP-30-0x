# 3.1.1.11 LAB: Essentials of the if-else statement

"""
Estimated time
10-20 minutes

Level of difficulty
Easy/Medium

Objectives
Familiarize the student with:
- Using the if-else instruction to branch the control path;
- Building a complete program that solves simple real-life problems.

Scenario
Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
- If the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
- If the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

Your task is to write a tax calculator.
- It should accept one floating-point value: the income.
- Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.

Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

Look at the code in the editor - it only reads one input value and outputs a result, so you need to complete it with some smart calculations.
Test your code using the data we've provided.

Test Data:
Sample input: 10000
Expected output: The tax is: 1244.0 thalers

Sample input: 100000
Expected output: The tax is: 19470.0 thalers

Sample input: 1000
Expected output: The tax is: 0.0 thalers

Sample input: -100
Expected output: The tax is: 0.0 thalers
"""

# Solution

income = float(input("Enter the annual income: "))

if income <= 0:
    tax = 0.0  # Great, no income. Guess you’re not paying taxes then... Must be nice

elif income <= 85528:
    # Calculating the "small fish" tax for those who don't make enough to be truly annoying
    tax = (income * 0.18) - 556.02
    if tax < 0:
        tax = 0.0  # Because, of course, negative taxes don’t exist. Don’t get too excited
else:
    surplus = income - 85528
    # The tax for people who actually make money
    tax = 14839.02 + (0.32 * surplus)


tax = round(tax, 2)  # Because precision is overrated


# The tax. Feel free to hate the system as much as I do
print("The tax is:", tax, "thalers")
