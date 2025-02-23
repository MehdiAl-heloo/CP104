"""
-------------------------------------------------------
[Assignment 4, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import day_name

day_num = int(input("Enter a number 1-7: "))

day = day_name(day_num)

print()
if day == "ERROR":
    print(f"{day}")
else:
    print(f"The corresponding day is {day}")
