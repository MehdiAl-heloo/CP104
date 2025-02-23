"""
-------------------------------------------------------
[Assignment 7, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports


def list_factors(number):
    """
    -------------------------------------------------------
    Makes a list of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: list = list_factors(numbers)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        list - the list of factors (list of int)
    ------------------------------------------------------
    """
    list = []
    i = 1
    x = 0
    while i < number:
        if number % i == 0:
            list.insert(x, i)
            x += 1
        i += 1
    return list


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    i = 0
    number_list = []
    num = int(input("Enter a positive number: "))
    while num != 0:
        if num > 0:
            number_list.insert(i, num)
            i += 1
        num = int(input("Enter a positive number: "))
    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    i = 0
    n = len(numbers)
    while i < n:
        index = numbers[i]
        if target_number == index:
            index_list.append(i)
        i += 1
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    i = 0
    while i < len(minuend):
        if minuend[i] in subtrahend:
            minuend.pop(i)
        else:
            i += 1
    return None


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    i = 0
    num = numbers[0]
    n = len(numbers)
    while i < n:
        if num > numbers[i]:
            in_order = False
            index = i
            i += len(numbers)
        elif num <= numbers[i]:
            num = numbers[i]
        i += 1
    return in_order, index
