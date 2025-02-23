"""
-------------------------------------------------------
[Lab 6, Task 15]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-26"
-------------------------------------------------------
"""
# Imports
from functions import statistics

n = int(input("How many numbers do you want to enter: "))

number = statistics(n)

print(f"Minimum, Maximum, Total, Average: {number}")
