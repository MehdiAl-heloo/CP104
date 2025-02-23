"""
-------------------------------------------------------
[Lab 4, Task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports
from functions import total_change

n = int(input("Number of Nickels: "))
d = int(input("Number of Dimes: "))
q = int(input("Number of Quarters: "))
l = int(input("Number of Loonies: "))
t = int(input("Number of Toonies: "))

total = total_change(n, d, q, l, t)

print()
print(f"Total: {total:.2f}")
