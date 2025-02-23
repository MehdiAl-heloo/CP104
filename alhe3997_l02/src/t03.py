"""
-------------------------------------------------------
[lab 2, task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Constants
LARGE_DOG_COST = 75
SMALL_DOG_COST = 50

big_groomed = int(input("Number of large dogs groomed: "))
small_groomed = int(input("Number of small dogs groomed: "))

profit = int(LARGE_DOG_COST * big_groomed + SMALL_DOG_COST * small_groomed)

print("Total earned for the day: $", profit)
