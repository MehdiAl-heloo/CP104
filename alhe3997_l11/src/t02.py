"""
-------------------------------------------------------
[Lab 11, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_char

rows = int(input("How many rows in the matrix: "))
cols = int(input("How many columns in the matrix: "))

matrix = generate_matrix_char(rows, cols)

print()
print(matrix)
