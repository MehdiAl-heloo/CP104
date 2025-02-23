"""
-------------------------------------------------------
[Lab 4, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports

from functions import square_pyramid

b = float(input("Enter the base of the pyramid: "))
h = float(input("Enter the height of the pyramid: "))

sp = square_pyramid(b, h)

print()
print("slant height, area, volume")
print(sp)
