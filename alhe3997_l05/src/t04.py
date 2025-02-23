"""
-------------------------------------------------------
[Lab 5, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports
from functions import closest

target = float(input("Enter the target value: "))
v1 = float(input("Enter the first value: "))
v2 = float(input("Enter the second value: "))

result = closest(target, v1, v2)

print()
print(f"The value {result} is closer")
