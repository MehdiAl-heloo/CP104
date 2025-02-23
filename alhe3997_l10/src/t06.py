"""
-------------------------------------------------------
[Lab 10, Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import number_stats

number_file = "C:/Users/mehdi/Downloads/numbers.txt"
fh = open(number_file, "r", encoding="utf-8")
smallest, largest, total, average = number_stats(fh)
fh.close()

print(f"{smallest:.2f} {largest:.2f} {total:.2f} {average:.2f}")
