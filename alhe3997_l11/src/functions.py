"""
-------------------------------------------------------
[Lab 11, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
import random


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []

    if value_type == "int":
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(random.randint(low, high))
            matrix.append(row)
    elif value_type == "float":
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(random.uniform(low, high))
            matrix.append(row)

    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    letters = "abcdefhijklmnopqrstuvwxyz"
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.choice(letters))
        matrix.append(row)

    return matrix


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    matrix = []

    for i in word_list:
        column = []
        for char in i:
            column.append(char)
        matrix.append(column)

    return matrix


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0
    rows = len(matrix)
    count = 0

    i = 0
    while i < rows:
        cols = len(matrix[i])
        j = 0
        while j < cols:
            if smallest > matrix[i][j]:
                smallest = matrix[i][j]
                total += matrix[i][j]
                count += 1
            elif largest < matrix[i][j]:
                largest = matrix[i][j]
                total += matrix[i][j]
                count += 1
            else:
                total += matrix[i][j]
                count += 1
            j += 1
        i += 1

    average = total/count

    return smallest, largest, total, average


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    rows = len(matrix)
    i = 0
    while i < rows:
        cols = len(matrix[i])
        j = 0
        while j < cols:
            new = matrix[i][j] * num
            matrix[i][j] = new
            j += 1
        i += 1

    return None
