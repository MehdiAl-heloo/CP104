"""
-------------------------------------------------------
[Assignment 9, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics

address_file = "C:/Users/mehdi/Downloads/addresses.txt"
file_handle = open(address_file, "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
file_handle.close()

print(f"{ucount}, {lcount}, {dcount}, {wcount}, {rcount}")
