"""
-------------------------------------------------------
[Lab 5, Function Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
from math import fabs


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    magic = day * month
    if magic == year:
        magic = True
    else:
        magic = False
    return magic


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    result1 = fabs(target - v1)
    result2 = fabs(target - v2)

    if result1 > result2:
        result = v2
    else:
        result = v1
    return result


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    if n > 10:
        numeral = False
    else:
        if n == 1:
            numeral = "I"
        elif n == 2:
            numeral = "II"
        elif n == 3:
            numeral = "III"
        elif n == 4:
            numeral = "IV"
        elif n == 5:
            numeral = "V"
        elif n == 6:
            numeral = "VI"
        elif n == 7:
            numeral = "VII"
        elif n == 8:
            numeral = "VIII"
        elif n == 9:
            numeral = "IX"
        else:
            numeral = "X"

    return numeral


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    TEN_FULL = 0.05
    FOUR_FULL = 0.015
    TEN_PART = 0.03
    FOUR_PART = 0.01
    OTHER = 0.02
    if status == "F":
        if years >= 10:
            new_salary = salary + (salary * TEN_FULL)
        elif years < 4:
            new_salary = salary + (salary * FOUR_FULL)
        else:
            new_salary = salary + (salary * OTHER)
    else:
        if years >= 10:
            new_salary = salary + (salary * TEN_PART)
        elif years < 4:
            new_salary = salary + (salary * FOUR_PART)
        else:
            new_salary = salary + (salary * OTHER)

    return new_salary


def ticket(age, student):
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket(age)
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    INFANT = 0
    SENIOR = 4
    STUDENT = 3
    SCHOOL_STUDENT = 1
    ADULT = 5
    KID = 2
    if age >= 65:
        price = SENIOR
    elif 10 <= age < 18:
        student = input("Are you a student at this school (Y/N): ")
        if student == "Y":
            price = SCHOOL_STUDENT
        else:
            price = STUDENT
    elif 18 <= age < 65:
        price = ADULT
    elif 3 <= age < 10:
        price = KID
    else:
        price = 0
    return price
