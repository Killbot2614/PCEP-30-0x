# 3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater

"""
Estimated time
5-15 minutes

Level of difficulty
Easy

Objectives
Familiarize the student with:
- Using the continue statement in loops;
- Modifying and upgrading the existing code;
- Reflecting real-life situations in computer code.

Scenario
Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab (3.1.2.10) and create a better, upgraded (pretty) vowel eater! Write a program that uses:
- A for loop;
- The concept of conditional execution (if-elif-else)
- The continue statement.

Your program must:
- Ask the user to enter a word;
- Use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
- Use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
- Assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it. Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the word_without_vowels variable.

Test your program with the data we've provided for you.

Test data
Sample input: Gregory
Expected output:
GRGRY

Sample input: abstemious
Expected output:
BSTMS

Sample input: IOUEA

Expected output:

"""

# Solution

word_without_vowels = ""
user_word = input("Enter a word: ").upper()
for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter
print(word_without_vowels)
