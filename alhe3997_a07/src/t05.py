"""
-------------------------------------------------------
[Assignment 7, Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
from functions import verify_sorted
from functions import list_positives

numbers = list_positives()

in_order, index = verify_sorted(numbers)

print(f"{in_order}, {index}")
