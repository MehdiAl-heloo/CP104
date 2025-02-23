"""
-------------------------------------------------------
[Lab 4, Task 11]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports
from functions import slope

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slp = slope(x1, y1, x2, y2)

print()
print("Slope:", slp)
