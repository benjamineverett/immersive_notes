'''
                     List comprehension and map function

Fill in each function below (there are 7).
Each function should be a one-liner.
You fill practice using 'map' and list comprehension with various datatypes.

Run "python -m doctest assignment_1a.py" at the command line to test your work.
'''

###############################################################################
#######                     Looking at Lists and Matrices
###############################################################################
def average_rows1(mat):
    return [sum(row)/len(row) for row in mat]

    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use list comprehension to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    pass

def average_rows2(mat):
    return list(map(lambda x: sum(x)/len(x), mat))
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use map to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    pass

def sort_rows(mat):
    return [row.sort() for row in mat]
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: 2 dimensional list of integers (matrix)

    Use list comprehension to modify each row of the matrix to be sorted.
    Notice that the matrix is modified in place

    Example:
    >>> M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    >>> sort_rows(M)
    >>> M
    [[2, 4, 5, 8], [3, 6, 7, 9]]
    '''
    pass

###############################################################################
#######                     Looking at Strings
###############################################################################
def word_lengths1(phrase):
    return [len(word) for word in phrase.split(' ')]

    '''
    INPUT: string
    OUTPUT: list of integers

    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths1("Welcome to the Data Science Immersive Program!")
    [7, 2, 7, 8]
    '''
    pass

def word_lengths2(phrase):
    return list(map(lambda x: len(x), phrase.split(' ')))

    '''
    INPUT: string
    OUTPUT: list of integers

    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths2("Welcome to the Data Science Immersive Program!!")
    [7, 2, 7, 8]
    '''
    pass

###############################################################################
#######                     Looking at Integers
###############################################################################
def even_odd1(L):
    return ['even' if num % 2 == 0 else 'odd' for num in L]

    '''
    INPUT: list of integers
    OUTPUT: list of strings

    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Example:
    >>> even_odd1([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    pass

def even_odd2(L):
    return list(map(lambda x: 'even' if x % 2 == 0 else 'odd', L))

    '''
    INPUT: list of integers
    OUTPUT: list of strings

    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Example:
    >>> even_odd2([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    pass
