"""
-------------------------------------------------------
[Assignment 3, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions

num1 = float(input("Please enter the numerator for the first fraction: "))
den1 = float(input("Please enter the denominator for the first fraction: "))
print()
num2 = float(input("Please enter the numerator for the second fraction: "))
den2 = float(input("Please enter the denominator for the second fraction: "))

fraction = multiply_fractions(num1, den1, num2, den2)

print()
print(f"Multiplied: in order of num, den, and product {fraction}")
