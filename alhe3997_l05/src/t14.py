"""
-------------------------------------------------------
[Lab 5, Task 14]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import ticket

age = int(input("How old are you? "))
student = "N"

print()
price = ticket(age, student)
print(f"Your ticket is ${price}")
