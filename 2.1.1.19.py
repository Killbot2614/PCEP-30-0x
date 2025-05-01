# 2.1.1.19 LAB: Formatting the output 

"""
Estimated time

5-15 minutes
Level of difficulty
Easy

Objectives:
- Experimenting with existing Python code;
- Discovering and fixing basic syntax errors;
- Becoming familiar with the print() function and its formatting capabilities.

Scenario:
We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition - learn from your mistakes and draw your own conclusions.

Try to:
- Minimize the number of print() function invocations by inserting the \n sequence into the strings
- Make the arrow twice as large (but keep the proportions)
- Duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
- Remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?

Do the same with some of the parentheses;
- Change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
- Replace some of the quotes with apostrophes; watch what happens carefully.
"""

# Solution

# 1. Minimize print() invocations
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n")

# 2. Duplicate arrows
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n" * 2)

# 3. NameError upon changing print() to Print()