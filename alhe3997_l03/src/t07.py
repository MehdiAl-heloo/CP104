"""
-------------------------------------------------------
[lab 3, task 7]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""

breakfast = float(input("Enter cost of breakfast: $"))
lunch = float(input("Enter cost of lunch: $"))
supper = float(input("Enter cost of supper: $"))
total = breakfast + lunch + supper

print()
print("Meal         Cost")
print(f"Breakfast    ${breakfast:>6.2f}")
print(f"Lunch        ${lunch:>6.2f}")
print(f"Supper       ${supper:>6.2f}")
print(f"Total        ${total:>6.2f}")
