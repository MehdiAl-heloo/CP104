"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""

flyer = int(input("Number of flyers: "))
volunteer = int(input("Number of volunteers: "))
flynum = flyer//volunteer
leftover = flyer % volunteer

print()
print("Flyers per volunteer:", flynum)
print("Flyers left over:", leftover)
