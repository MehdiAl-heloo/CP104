"""
-------------------------------------------------------
[Assignment 6, Task 3]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports
from functions import interest_table

principal_amount = float(input("Principal: $"))
interest_rate = float(input("Interest Rate: %"))
payment = float(input("Monthly Payment: $"))

interest_table(principal_amount, interest_rate, payment)
