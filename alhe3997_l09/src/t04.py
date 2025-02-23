"""
-------------------------------------------------------
[Lab 9, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import validate_code

product_code = str(input("Enter the product code: "))

category, digits, qualifiers = validate_code(product_code)

print()
print(f"{category} {digits} {qualifiers}")
