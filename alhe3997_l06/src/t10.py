"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-26"
-------------------------------------------------------
"""
# Imports
from functions import treadmill

burnt_per_minute = float(input("Calories burning per minute: "))
start = int(input("Start time in minutes: "))
end = int(input("End time in minutes: "))
inc = int(input("Increment in minutes: "))

treadmill(burnt_per_minute, start, end, inc)
