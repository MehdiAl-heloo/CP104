"""
-------------------------------------------------------
[Assignment 6, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import count_of_digits

number = int(input("Please enter an integer: "))

digits = count_of_digits(number)

print()
print(f"{digits} digit(s) in {number}")
