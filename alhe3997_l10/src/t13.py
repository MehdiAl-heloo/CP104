"""
-------------------------------------------------------
[Lab 10, Task 13]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import file_copy

words_file = "C:/Users/mehdi/Downloads/words.txt"
new_words_file = "new_words.txt"
fh_1 = open(words_file, "r", encoding="utf-8")
fh_2 = open(new_words_file, "w", encoding="utf-8")
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()

fh_2 = open(new_words_file, "r", encoding="utf-8")
print(fh_2.read())
fh_2.close()
