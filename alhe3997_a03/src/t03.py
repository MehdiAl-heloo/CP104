"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import extract_date

date_number = int(input("Please input a date in YYYYMMDD format: "))

date = extract_date(date_number)

print()
print(f"The date is {date}")
