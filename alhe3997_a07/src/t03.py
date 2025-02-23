"""
-------------------------------------------------------
[Assignment 7, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
from functions import get_indexes
from functions import list_positives

numbers = list_positives()

target_number = int(input("Enter the target number: "))

index_list = get_indexes(numbers, target_number)

print()
print(f"{index_list}")
