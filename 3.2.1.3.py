#  3.2.1.3 LAB: Essentials of the while loop - Guess the secret number

"""
Estimated time:
15 minutes

Level of difficulty:
Easy

Objectives:
Familiarize the student with:
- Using the while loop;
- Reflecting real-life situations in computer code.

Scenario:
A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way so that the code:
- Will ask the user to enter an integer number;
- Will use a while loop;
- Will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."

The magician is counting on you! Don't disappoint him.

EXTRA INFO:
By the way, look at the print() function. The way we've used it here is called multi-line printing. You can use triple quotes to print strings on multiple lines in order to make text easier to read, or create a special text-based design. Experiment with it.
"""

# Solution

secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    number = int(input("Guess the secret number: "))
    if number == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")

# Solution 2

# secret_number = 777
# guess_count = 0
# first_wrong = True

# print(
#     """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)

# while True:
#     number = int(input("Guess the secret number: "))
#     guess_count += 1
#     if number == secret_number:
#         print("Well done, muggle! You are free now.")
#         print(f"It took you {guess_count} guesses.")
#         break
#     else:
#         if first_wrong:
#             print("Ha ha! You're stuck in my loop!")
#             first_wrong = False

#         if number < secret_number:
#             print("Too low! Try again.")
#         else:
#            print("Too high! Try again.")
