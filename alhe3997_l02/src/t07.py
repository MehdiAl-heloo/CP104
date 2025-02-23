"""
-------------------------------------------------------
[lab 2, task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

flyer = int(input("Number of flyers: "))
volunteer = int(input("Number of volunteers: "))
flynum = flyer//volunteer
leftover = flyer % volunteer

print()
print("Flyers per volunteer:", flynum)
print("Flyers left over:", leftover)
