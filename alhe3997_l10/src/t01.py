"""
-------------------------------------------------------
[Lab 10, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_record

n = int(input("Which line do you want to read: "))

customer_file = "C:/Users/mehdi/Downloads/customers.txt"
fh = open(customer_file, "r", encoding="utf-8")
result = customer_record(fh, n)
fh.close()

print(f"{result}")
