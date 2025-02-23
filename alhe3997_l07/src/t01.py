"""
-------------------------------------------------------
[Lab 7, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import hi_lo_game

high = int(input("Guess a number between 1 up to the number of your choice: "))

count = hi_lo_game(high)

print(f"It took you {count} tries!")
