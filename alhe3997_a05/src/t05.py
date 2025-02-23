"""
-------------------------------------------------------
[Assignment 5, Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports
from functions import range_addition

start = int(input("Start: "))
increment = int(input("Increment: "))
count = int(input("Count: "))

total = range_addition(start, increment, count)

print()
print(f"Total: {total}")
