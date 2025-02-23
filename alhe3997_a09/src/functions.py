"""
-------------------------------------------------------
[Assignment 9, Functions Library]
-------------------------------------------------------
Author:  Mehdi Al-heloo
ID:      169063997
Email:   alhe3997@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports


def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = file_handle.readlines()
    i = 0

    if len(lines) < count:
        while i < len(lines):
            line = lines[i].strip()
            print(f"{line}")
            i += 1
    else:
        while i < count:
            line = lines[i].strip()
            print(f"{line}")
            i += 1
    return None


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    lines = file_handle.read().split(',')

    for i in lines:
        if i.strip().isdigit():
            num = int(i.strip())
            if num > 0:
                number_list.append(num)

    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    lines = file_handle.read()

    for i in lines:
        if i.isupper():
            ucount += 1
        elif i.islower():
            lcount += 1
        elif i.isdigit():
            dcount += 1
        elif i.isspace():
            wcount += 1
        else:
            rcount += 1

    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = fh_read.readlines()
    line_number = 0

    for i in lines:
        fh_write.write(f"[{line_number}] {i}")
        line_number += 1

    return None


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    total = 0
    count = 0
    l_id = 0
    h_id = 0
    lines = file_handle.readlines()
    lowest = float(101)
    highest = float(-1)

    for i in lines:
        surname, forename, student_id, mark = i.strip().split(',')
        mark = float(mark)
        if mark < lowest:
            lowest = mark
            l_id = student_id
        elif mark > highest:
            highest = mark
            h_id = student_id
        total += mark
        count += 1

    if count > 0:
        avg = total/count
    else:
        avg = 0

    return l_id, h_id, avg
