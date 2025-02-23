"""
-------------------------------------------------------
[Lab 9, Task 10]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import text_analyze

txt = str(input("Enter some text: "))

uppr, lowr, dgts, whtspc = text_analyze(txt)

print()
print(f"{uppr} {lowr} {dgts} {whtspc}")
