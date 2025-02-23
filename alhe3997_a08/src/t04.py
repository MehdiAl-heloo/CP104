"""
-------------------------------------------------------
[Assignment 8, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import valid_isbn

isbn = str(input("Enter Isbn: "))

is_valid = valid_isbn(isbn)

print()
print(f"Valid Isbn: {is_valid}")
