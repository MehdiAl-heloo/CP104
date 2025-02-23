"""
-------------------------------------------------------
[Assignment 2, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
num = int(input("Enter a positive two-digit number: "))

calculation = ((num/10)//1) * 10
first = calculation/10
second = num - calculation


difference = int(first - second)

print()
print("The difference of the digits of", num, 'is', difference)
