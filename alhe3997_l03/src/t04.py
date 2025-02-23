"""
-------------------------------------------------------
[lab 3, task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""

num = float(input("Enter number: "))
percent = float(input("Enter percent: "))
discount = (percent/100.0) * num

print(f"A {percent:.1f} percent discount on {num:.1f} is {discount:.1f}")
