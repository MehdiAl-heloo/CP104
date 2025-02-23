"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import generate_integer_list
from functions import linear_search

n = int(input("How many numbers do you want in the list: "))
low = int(input("What is the low value of the range: "))
high = int(input("What is the high value of the range: "))

values = generate_integer_list(n, low, high)

print(values[-100:100])

value = int(input("What number do you want to search for? "))
index = linear_search(values, value)

print(index)
