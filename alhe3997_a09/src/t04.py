"""
-------------------------------------------------------
[Assignment 9, Task 4]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering

wilde_file = "C:/Users/mehdi/Downloads/wilde.txt"
new_wilde_file = "wilde_numbered.txt"
fh_read = open(wilde_file, "r", encoding="utf-8")
fh_write = open(new_wilde_file, "w", encoding="utf-8")
line_numbering(fh_read, fh_write)
fh_read.close()
fh_write.close()

fh_write = open(new_wilde_file, "r", encoding="utf-8")
print(fh_write.read())
fh_write.close()
