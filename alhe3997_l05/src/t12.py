"""
-------------------------------------------------------
[Lab 5, Task 12]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-16"
-------------------------------------------------------
"""
# Imports
from functions import pay_raise

status = input("What is your employment type (F/P): ")
years = float(input("How many years have you been working: "))
salary = float(input("What is your current salary: "))

new_salary = pay_raise(status, years, salary)

print()
print(f"Your salary after the raise is: {new_salary:.2f}")
