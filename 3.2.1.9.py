#  3.2.1.9 LAB: The break statement - Stuck in a loop

"""
Estimated time:10-20 minutes
Level of difficulty: Easy
Objectives:
Familiarize the student with:
- Using the break statement in loops;
- Reflecting real-life situations in computer code.

Scenario:
The break statement is used to exit/terminate a loop.
Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.
"""

secret_word = "chupacabra"
while True:
    word = input("Enter a word: ")
    if word == secret_word:
        print("You've successfully left the loop.")
        break
