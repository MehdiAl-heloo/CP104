"""
-------------------------------------------------------
[Assignment 8, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import common_end

str1 = str(input("Enter the first word: "))
str2 = str(input("Enter the second word: "))

suffix = common_end(str1, str2)

print()
print(f"{suffix}")
