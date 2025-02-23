"""
-------------------------------------------------------
[Assignment 4, Task 2]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports
from functions import pollution_ranking

air_quality_index = int(input("Please enter the AIR QUALITY INDEX: "))

pollution = pollution_ranking(air_quality_index)

print()
if pollution == "ERROR":
    print(f"{pollution}")
else:
    print(f"The air quality is {pollution}")
