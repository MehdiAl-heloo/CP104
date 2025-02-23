"""
-------------------------------------------------------
[Lab 7, Task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import meal_costs

b_total, l_total, s_total, a_total = meal_costs()

print()
print(
    f"Breakfast, Lunch, Supper, and Total among the day(s): {b_total:.2f} {l_total:.2f} {s_total:.2f} {a_total:.2f}")
