"""
-------------------------------------------------------
[Lab 6, Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-26"
-------------------------------------------------------
"""
# Imports
from functions import draw_rectangle

height = int(input("Input the height of the rectangle: "))
width = int(input("Input the width of the rectangle: "))
char = str(input("Input the character you want to use: "))

print()
draw_rectangle(height, width, char)
