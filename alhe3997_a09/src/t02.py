"""
-------------------------------------------------------
[Assignment 9, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

number_file = "C:/Users/mehdi/Downloads/numbers (1).txt"
file_handle = open(number_file, "r", encoding="utf-8")
number_list = read_integers(file_handle)
file_handle.close()

print(f"{number_list}")
