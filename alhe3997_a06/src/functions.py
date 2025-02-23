"""
-------------------------------------------------------
[Assignment 6, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports


def total_wins():
    """
    -------------------------------------------------------
    Asks the user to enter a series of strings and counts how 
    many times purple and gold have been entered.
    Use: purple, gold = total_wins()
    -------------------------------------------------------
    Returns:
        purple - The amount of times purple was entered - (int >= 0)
        gold - The amount of time gold was entered - (int >= 0)
    ------------------------------------------------------
    """
    purple = 0
    gold = 0
    count = str(input("Enter the winning team: "))
    while count != "":
        if count == "purple":
            purple += 1
            count = str(input("Enter the winning team: "))
        elif count == "gold":
            gold += 1
            count = str(input("Enter the winning team: "))
        else:
            count = str(input("Enter the winning team: "))
    return purple, gold


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    i = 1
    prime = False
    while i < number:
        if number % i == 0:
            prime = False
        else:
            prime = True
        i += 1
    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    month = 1
    interest = (interest_rate/12)/100
    print("""----------------------------------
Month Interest   Payment   Balance
----------------------------------""")
    while principal_amount > 0:
        interest = principal_amount * ((interest_rate/12)/100)
        if payment < principal_amount:
            principal_amount = principal_amount + interest - payment
            print(
                f"{month:5d} {interest:8.2f} {payment:9.2f} {principal_amount:9.2f}")
        elif payment > principal_amount:
            payment = principal_amount + interest
            principal_amount = 0
            print(
                f"{month:5d} {interest:8.2f} {payment:9.2f} {principal_amount:9.2f}")
        month += 1
    return None


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    divide = 1
    if number > 0:
        while number/divide >= 1:
            digits += 1
            divide = divide * 10
    elif number < 0:
        while number/divide <= -1:
            digits += 1
            divide = divide * 10
    else:
        digits = 1
    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    i = 1
    total = 0
    while i < number:
        if number % i == 0:
            total += i
        i += 1
    return total
