"""
-------------------------------------------------------
[Assignment 2, Task 5]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wall = float(input("Wall height (m): "))
costc = float(input("Cost of concrete ($/m^3): "))
costb = float(input("Cost of bricks ($/m^2): "))

concrete = length * width * height
cost1 = concrete * costc
bricks = (2 * width * wall) + (2 * length * wall)
cost2 = bricks * costb
total = cost1 + cost2

print()
print(f"Concrete needed for foundation (m^3): {concrete:,.2f}")
print(f"Cost of concrete: ${cost1:,.2f}")
print(f"Bricks needed for walls (m^2): {bricks:,.2f}")
print(f"Cost of bricks: ${cost2:,.2f}")
print(f"Total cost: ${total:,.2f}")
