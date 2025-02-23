"""
-------------------------------------------------------
[Lab 9, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    hydroxide = chemical.endswith("OH")
    return hydroxide


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    n = len(product_code)
    category = False
    digits = False
    qualifiers = False
    if n >= 3:
        upper_category = product_code[0:3].upper()
        if product_code[0:3] == upper_category:
            if product_code[0:3].isalpha() == True:
                category = True
    if n >= 7:
        if product_code[3:7].isdigit() == True:
            digits = True
    if n >= 8:
        upper_qualifier = product_code[7].upper()
        if product_code[7] == upper_qualifier:
            qualifiers = True
    return category, digits, qualifiers


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    digits = False
    upper = False
    lower = False
    n = len(password)
    if n < 8:
        print("Not long enough")

    i = 0
    while i < n:
        if password[i].isdigit() == True:
            digits = True
            i += n
        else:
            i = i + 1
    if digits == False:
        print("No digits")

    i = 0
    while i < n:
        if password[i].isupper() == True:
            upper = True
            i += n
        else:
            i = i + 1
    if upper == False:
        print("No upper case")

    i = 0
    while i < n:
        if password[i].islower() == True:
            lower = True
            i += n
        else:
            i = i + 1
    if lower == False:
        print("No lower case")

    return None


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    n = len(txt)
    i = 0
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    while i < n:
        if txt[i].isupper() == True:
            uppr += 1
        i += 1

    i = 0
    while i < n:
        if txt[i].islower() == True:
            lowr += 1
        i += 1

    i = 0
    while i < n:
        if txt[i].isdigit() == True:
            dgts += 1
        i += 1

    i = 0
    while i < n:
        if txt[i].isspace() == True:
            whtspc += 1
        i += 1

    return uppr, lowr, dgts, whtspc
