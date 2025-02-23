"""
-------------------------------------------------------
[Lab 5, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports
from functions import magic_date

day = int(input("What day were you born (day as number): "))
month = int(input("What month were you born (month as number): "))
year = int(input("What year were you born (last two digits of year): "))

magic = magic_date(day, month, year)

print()
print(f"Is your birth date is magic: {magic}")
