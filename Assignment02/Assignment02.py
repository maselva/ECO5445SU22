# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:43:35 2022
@author: mselv
"""
"""
Number 2
"""

Johns_age = 2  # Integer

nice = 2.0  # Float

password = 10j  # Complex

slogan = "2 Cool for School"  # String

warm = True  # Bool

# How did you identify these? Looking for 'type()' (-5)
"""
Number 3
"""

A = [2, 2.0, 10j, '2 Cool for School', 'True'] # Looking for reference to previous variables: A = [Johns_age, nice, password, slogan, warm] 

"""
Number 4
"""

B = 'I like pie more than cake'
#    0123456789012345678901234

B[:6]

B[7:15]

B[16:25]

B[:6] + ' ' + B[11:15] + ' ' + B[21:25]

"""
Number 5
"""


def foo_bar(num): # didn't provide proper header ex: def foobar(value: int) -> str: (-5)
    """ Determine if the value is a multiple of 3, 5, or 15.
    >>> foo_bar(6)
    'foo'
    >>> foo_bar(20)
    'bar'
    >>> foo_bar(45)
    'foobar'
    >>> foo_bar(61)
    'Not a multiple of 3, 5, or 15'
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'foobar'
    elif num % 3 == 0:
        return 'foo'
    elif num % 5 == 0:
        return 'bar'
    else:
        return 'Not a multiple of 3, 5, or 15'
    
# Did not provide test cases. Inputting a string breaks code (-5)
foo_bar(10)
foo_bar("cat")
foo_bar(90)
foo_bar(27)
foo_bar(101)
