"""
-------------------------------------------------------
[assignment 1, task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-26"
-------------------------------------------------------
"""

principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
numy = int(input("Number of years: "))
compound = int(input("Number of times interest compounded per year: "))

interest1 = interest/100
balance = principal * ((1 + interest1/compound)**(compound*numy))

print()
print("Balance: $", balance)
