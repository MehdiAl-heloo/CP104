"""
-------------------------------------------------------
[Lab 5, Task 8]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports
from functions import roman_numeral

n = int(input("Please enter a number 1-10 to convert into it's Roman numeral: "))

numeral = roman_numeral(n)

print()
print(f"{n} --> {numeral}")
