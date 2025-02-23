"""
-------------------------------------------------------
[Lab 11, Task 13]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import matrix_scalar_multiply

matrix = [[2, 0, -1, 1], [10, 4, -5, 9], [-6, 3, 6, 0]]

print(f"{matrix}")

num = int(input("Enter a number to multiply the matrix by: "))

matrix_scalar_multiply(matrix, num)

print(f"{matrix}")
