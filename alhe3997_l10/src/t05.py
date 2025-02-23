"""
-------------------------------------------------------
[Lab 10, Task 10]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_append

fields = ['35612', 'David', 'Brown', 237.56, '2008-10-10']

customer_file = "C:/Users/mehdi/Downloads/customers.txt"
fh = open(customer_file, "a", encoding="utf-8")
customer_append(fh, fields)
fh.close()

fh = open(customer_file, "r", encoding="utf-8")
print(fh.read())
fh.close
