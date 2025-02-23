"""
-------------------------------------------------------
[Lab 9, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import is_hydroxide

chemical = str(input("Enter a chemical formula: "))

hydroxide = is_hydroxide(chemical)

print()
print(f"Hydroxide: {hydroxide}")
