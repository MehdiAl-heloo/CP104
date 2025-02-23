"""
-------------------------------------------------------
[Assignment 5, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    if number < 0:
        product = "*Error*"
    else:
        product = 1
        for i in range(1, number + 1, 1):
            product = product * i
    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a tread mill over
    a time range in increments of five. Given time and calories 
    burnt per minute
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burnt per minute (float > 0)
        minutes - time spent on tread mill (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    if minutes or per_min < 0:
        print("*Error*")
    else:
        for i in range(5, minutes + 1, 5):
            calories = i * per_min
            print(f"{i:3d} {calories:.1f}")
    return None


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an arrow of # pointing up, with a given amount
    of rows.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows for the arrow (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    space_start = rows - 1
    space_middle = 1
    if rows < 0:
        print("*Error*")
    else:
        for i in range(0, rows, 1):
            start = " " * space_start
            middle = " " * space_middle
            if i == 0:
                print(f"{start}#")
                space_start -= 1
            else:
                print(f"{start}#{middle}#")
                space_start -= 1
                space_middle += 2
    return None


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    print("       ", end="")
    for i in range(start_num, stop_num + 1, 1):
        if i != stop_num:
            print(f"{i:5d}", end="")
        else:
            print(f"{i:5d}")
    print("       ", end="")
    for i in range(start_num, stop_num + 1, 1):
        if i != stop_num:
            print(f"-----", end="")
        else:
            print(f"-----")
    for i in range(start_num, stop_num + 1, 1):
        print(f"{i:5d} |", end="")
        for x in range(start_num, stop_num + 1, 1):
            multiplication = i * x
            if x != stop_num:
                print(f"{multiplication:5d}", end="")
            else:
                print(f"{multiplication:5d}")
    return None


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(0, count, 1):
        total += start + (i * increment)
    return total
