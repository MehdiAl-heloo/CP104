"""
-------------------------------------------------------
[Assignment 4, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import largest_average

val1 = float(input("Enter the first value: "))
val2 = float(input("Enter the second value: "))
val3 = float(input("Enter the third value: "))

average = largest_average(val1, val2, val3)

print()
print(f"The average between the two largest values is {average:.2f}")
