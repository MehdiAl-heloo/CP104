"""
-------------------------------------------------------
[Assignment 8, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports


def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    n = len(sentence)
    i = 0
    w = 0
    spaced = ""
    while i < n:
        if sentence[i].isupper():
            if w != 0:
                spaced = spaced + " "
            spaced = spaced + sentence[w:i].lower()
            w = i
        i += 1
    spaced += " " + sentence[w:].lower()
    spaced = spaced.capitalize()
    return spaced


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    n = len(string)
    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        pluralized = string + "es"
    elif string.endswith("y") or string.endswith("ay") or string.endswith("oy"):
        pluralized = string[0:n - 1] + "ies"
    else:
        pluralized = string + "s"
    return pluralized


def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    suffix = ""
    n1 = len(str1)
    n2 = len(str2)
    counter = 1
    if str1[n1-1] == str2[n2-1]:
        while str1[n1 - counter] == str2[n2 - counter]:
            if counter < n1 or counter < n2:
                suffix = str1[n1 - counter:]
                counter += 1

    return suffix


def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    n = len(isbn)
    groups = isbn.split('-')
    five = True
    first = True
    final = True
    length = True
    d = True

    if len(groups[4]) != 1:
        final = False
    elif isbn[n-2].isdigit() != False:
        final = False

    if len(groups) != 5:
        five = False

    if groups[0] != "978" and groups[0] != "979":
        first = False

    if len(isbn) != 17:
        length = False

    i = 0
    while i < len(groups):
        if groups[i].isalpha():
            d = False
            i += len(groups)
        i += 1

    if five and first and final and length and d == True:
        is_valid = True
    else:
        is_valid = False

    return is_valid


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True
    i = 0
    while i < len(words) - 1:
        if words[i][-1].lower() != words[i + 1][0].lower():
            word_chain = False
        i += 1

    return word_chain
