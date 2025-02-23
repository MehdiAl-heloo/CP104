"""
-------------------------------------------------------
[Assignment 7, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
from functions import list_subtract
from functions import list_positives

minuend = list_positives()
print()
subtrahend = list_positives()

print(f"minuend before: {minuend}")
list_subtract(minuend, subtrahend)
print(f"minuend after:  {minuend}")
