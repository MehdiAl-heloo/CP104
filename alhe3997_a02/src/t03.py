"""
-------------------------------------------------------
[Assignment 2, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""

date = int(input("Enter a date in the format YYYYMMDD: "))

calc_year = ((date/10000)//1) * 10000
calc_month = (((date - calc_year)/100)//1) * 100

year = int(calc_year/10000)
month = int(calc_month/100)
day = int(date - (((date/100)//1))*100)

print()
print(f"The reformatted date: {year}/{month:02d}/{day:02d}")
