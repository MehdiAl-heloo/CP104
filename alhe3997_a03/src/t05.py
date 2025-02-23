"""
-------------------------------------------------------
[Assignment 3, Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import falling_distance

falling_time = float(
    input("How long did it take the object to hit the ground: "))

distance = falling_distance(falling_time)

print()
print(f"The object fell from {distance} meters")
