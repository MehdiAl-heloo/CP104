"""
-------------------------------------------------------
[Lab 6, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-26"
-------------------------------------------------------
"""
# Imports
from functions import sum_even

num = int(input("Input number: "))

total = sum_even(num)

print()
print(f"{total} is the sum of all even numbers in your number")
