"""
-------------------------------------------------------
[lab 2, task 6]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""

mortgage = int(input("Mortgage principal ($): "))

durationy = int(input("Number of years: "))
durationm = float(durationy * 12)

interesty = float(input("Yearly interest rate (%): "))
interestm = float((interesty/12)/100)

monthly = float(mortgage * ((interestm * ((1 + interestm) ** durationm)) /
                            (((1 + interestm) ** durationm) - 1)))

print()
print("The monthly payments are: $", monthly)
