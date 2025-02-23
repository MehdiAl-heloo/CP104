"""
-------------------------------------------------------
[Assignment 4, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import colour_combine

rgb_colour1 = str(input("Enter the first RGB colour: "))
rgb_colour2 = str(input("Enter the second RGB colour: "))

rgb_colour = colour_combine(rgb_colour1, rgb_colour2)

print()

if rgb_colour == "ERROR":
    print(f"{rgb_colour}")
else:
    print(f"{rgb_colour1} and {rgb_colour2} make {rgb_colour}")
