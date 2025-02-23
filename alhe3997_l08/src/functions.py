"""
-------------------------------------------------------
[Lab 8, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
from random import randint


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    week = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    d = d - 1
    name = week[d]
    return name


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    for i in range(0, n, 1):
        d = randint(low, high)
        values.insert(i, d)
    return values


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = values[0]
    largest = values[0]
    total = 0
    i = 0
    n = len(values)
    while i < n:
        if values[i] < smallest:
            smallest = values[i]
        elif values[i] > largest:
            largest = values[i]
        total += values[i]
        i = i + 1
    average = total/n

    return smallest, largest, total, average


def linear_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns its index.
    User: index = linear_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        index - the index of the location of value in values,
            -1 if not found (int).
    -------------------------------------------------------
    """
    i = 0
    n = len(values)
    while i < n:
        if values[i] == value:
            index = i
            i += n
        else:
            index = -1
        i = i + 1
    if n == 0:
        index = -1
    return index
