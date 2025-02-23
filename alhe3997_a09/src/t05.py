"""
-------------------------------------------------------
[Assignment 9, Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import student_stats

students_file = "C:/Users/mehdi/Downloads/students.txt"
file_handle = open(students_file, "r", encoding="utf-8")
l_id, h_id, avg = student_stats(file_handle)
file_handle.close()

print(f"{l_id}, {h_id}, {avg}")
