"""
-------------------------------------------------------
[Assignment 3, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres

square_feet = float(input("Input the square feet to be converted to acres: "))

acres = footage_to_acres(square_feet)

print()
print(f"{square_feet} square feet in acres is {acres} acres")
