"""
-------------------------------------------------------
[Lab 9, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import parse_code

product_code = str(input("Enter the product code: "))

pc, pi, pq = parse_code(product_code)

print()
print(f"{pc} {pi} {pq}")
