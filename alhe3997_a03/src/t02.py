"""
-------------------------------------------------------
[Assignment 3, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import lawn_mow_time

length = float(input("Length of the lawn in meters: "))
width = float(input("Width of the lawn in meters: "))
speed = float(input("Square meters cut per minute: "))

time = lawn_mow_time(length, width, speed)

print()
print(f"It will take {time} minutes to cut the lawn")
