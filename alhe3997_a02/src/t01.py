"""
-------------------------------------------------------
[Assignment 2, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Constants
ANNUAL_TAX = 0.185

sales = float(input("Enter the total sales: $"))

tax = float(sales * ANNUAL_TAX)

print()
print("Projected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {sales:,.2f}")
print("Annual tax:    % 18.50")
print("--------------------------")
print(f"Tax:           $ {tax:,.2f}")
