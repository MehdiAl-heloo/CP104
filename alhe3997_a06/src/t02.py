"""
-------------------------------------------------------
[Assignment 6, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import detect_prime

number = int(input("Enter a number to check if it is a prime number: "))

prime = detect_prime(number)

print()
print(f"Prime: {prime}")
