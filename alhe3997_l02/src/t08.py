"""
-------------------------------------------------------
[lab 2, task 8]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg):"))
bmi_limit = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

bmi = weight / (height**2)
bmi_prime = bmi / bmi_limit

print()
print("Body Mass Index (kg/m^2) =", bmi)
print("BMI Prime =", bmi_prime)
