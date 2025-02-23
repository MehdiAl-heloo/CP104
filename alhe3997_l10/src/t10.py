"""
-------------------------------------------------------
[Lab 10, Task 10]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word

word = str(input("Word to count: "))

words_file = "C:/Users/mehdi/Downloads/words.txt"
fh = open(words_file, "r", encoding="utf-8")
count = count_frequency_word(fh, word)
fh.close()

print(f"{word} appeared {count} times")
