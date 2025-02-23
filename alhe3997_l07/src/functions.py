"""
-------------------------------------------------------
[Lab 7, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 1
    number = randint(1, high)
    guess = int(input("Guess: "))
    while guess != number:
        if guess > number:
            print("Too high, try again.")
            guess = int(input("Guess: "))
            count += 1
        elif guess < number:
            print("Too low, try again.")
            guess = int(input("Guess: "))
            count += 1
    print("Congratulations - Good Guess!")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 2
    while power < target:
        power = power**2
    if power >= target and target <= 1:
        power = 1
    return power


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    number = 1
    final = 0
    while final < target:
        final = final + number**2
        number += 1
    if final == target and target == 0:
        final = 1
    return final


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    day = 1
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0
    next_day = "Y"
    while next_day != "N":
        print(f"For day {day}")
        print()
        breakfast = float(input("How much was breakfast? $"))
        lunch = float(input("How much was lunch? $"))
        supper = float(input("How much was supper? $"))
        total = breakfast + lunch + supper
        print(f"Your total for today was: ${total}")
        b_total += breakfast
        l_total += lunch
        s_total += supper
        a_total += total
        next_day = str(input("Were you away another day (Y/N)? "))
        day += 1
    return b_total, l_total, s_total, a_total


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    OVERTIME = 40
    OVERTIME_RATE = 1.5
    TAX_RATE = 0.03625
    total = 0
    average = 0
    id = int(input("Employee ID: "))
    employees = 0
    while id != 0:
        hourly = float(input("Hourly wage rate: $"))
        hours = float(input("Hours worked: "))
        if hours <= 40:
            net = (hours * hourly) - ((hours * hourly) * TAX_RATE)
        elif hours > 40:
            net = (40 * hourly) + ((hours - OVERTIME) * (hourly * OVERTIME_RATE)) - \
                (((40 * hourly) + ((hours - OVERTIME) *
                 (hourly * OVERTIME_RATE))) * TAX_RATE)
        print(f"Net payment for employee {id}: ${net:.2f}")
        employees += 1
        total += net
        average = total/employees
        print()
        id = int(input("Employee ID: "))
    return total, average
