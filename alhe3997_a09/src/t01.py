"""
-------------------------------------------------------
[Assignment 9, Task 1]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from functions import file_top

count = int(input("How many lines do you want to read: "))

students_file = "C:/Users/mehdi/Downloads/students.txt"
file_handle = open(students_file, "r", encoding="utf-8")
file_top(file_handle, count)
file_handle.close()


total = 0
stop = 5

for i in range(stop):
    total = total + i
    i = i + stop
print(total)
