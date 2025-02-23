"""
-------------------------------------------------------
[lab 2, task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

# Constants
FAHRENHEIT_FREEZING = 32

celsius = int(input("Temperature (C): "))

f_to_c = int(celsius * (9/5) + FAHRENHEIT_FREEZING)
print("Temperature (F):", f_to_c)
