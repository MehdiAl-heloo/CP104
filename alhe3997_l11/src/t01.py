"""
-------------------------------------------------------
[Lab 11, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num

rows = int(input("How many rows in the matrix: "))
cols = int(input("How many columns in the matrix: "))
low = int(input("What is the lowest number in the matrix: "))
high = int(input("What is the highest number in the matrix: "))
value_type = str(input("What value type (float/int): "))

matrix = generate_matrix_num(rows, cols, low, high, value_type)

print()
print(f"{matrix}")
