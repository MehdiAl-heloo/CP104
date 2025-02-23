"""
-------------------------------------------------------
[Assignment 6, Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import factor_summation

number = int(input("Please enter an integer: "))

total = factor_summation(number)

print()
print(f"The sum of all the factors (not including the number itself): {total}")
