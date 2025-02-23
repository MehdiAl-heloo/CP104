"""
-------------------------------------------------------
[Lab 8, Task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import generate_integer_list
from functions import list_stats

n = int(input("How many numbers do you want in the list: "))
low = int(input("What is the low value of the range: "))
high = int(input("What is the high value of the range: "))

values = generate_integer_list(n, low, high)

smallest, largest, total, average = list_stats(values)

print(values[-100:100])
print(f"{smallest} {largest} {total} {average:.2f}")
