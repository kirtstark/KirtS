"""
:mod:`source.source1` -- Example source code
============================================

The following example code provides story question answers
"""

import math
import getpass

def get_fibonacci(a=0):
    """
    returns the nth number in the fibonacci sequence

    :param a: line a
    :type a: int, float

    :return: fibonacci number
    :rtype: int
    """

    if a < 0:
        return 'I cannot process a negative number'

    if a == 0:
        return 0

    if a == 1 or a == 2:
        return 1

    b = 1
    c = 1

    x = int(round(a))
    for num in range(2, x):
        d = b + c
        b = c
        c = d

    return d


def get_some_pi(n=0):
    """
    returns the nth number in pi, up to the 13th digit

    :param n: line a
    :type n: int, float

    :return: nth digit number
    :rtype: int
    """

    if n <= 0:
        return 'The number must be greater than zero'

    if n > 12:
        return 'taken too far'

    try:
        return int(str(math.pi).replace('.', '')[int(round(n)) - 1])
    except ValueError:
        return "error in digit"


def get_the_door():
    """
    returns a string response with the username taken from the open account

    :param na
    :type na

    :return: a sentence response that includes the system username
    :rtype: str
    """

    return 'I\'m afraid I can\'t do that ' + getpass.getuser()

def convert_unit_to_unit(x=0, unit1='', unit2=''):
    """
    returns a string response with the username taken from the open account

    :param x: line x
    :type x: float

    :param unit1: line unit1
    :type unit1: string:

    param unit2: line unit2
    :type unit2: string

    :return: a float value of a number converted from one unit to another, or error code
    :rtype: float, string
    """
    if unit1 == "inches":
        unit1 = "inch"

    if unit2 == "inches":
        unit2 = "inch"

    if unit1[-1] == 's' and unit1.__len__ > 1:
        unit1 = str(unit1[0:-1])

    if unit2[-1] == 's' and unit2.__len__ > 1:
        unit2 = str(unit2[0:-1])

    if unit1 == "centimeter" and unit2 == "inch":
        return x * 0.39370079

    elif unit1 == "inch" and unit2 == "centimeter":
        return x / 0.39370079

    elif unit1 == "quart" and unit2 == "liter":
        return x * 0.94635295

    elif unit1 == "liter" and unit2 == "quart":
        return x / 0.94635295

    elif unit1 == "fahrenheit" and unit2 == "centigrade":
        return (x - 32) * 5 / 9

    elif unit1 == "centigrade" and unit2 == "fahrenheit":
        return x * 9 / 5 + 32

    elif unit1 == "pound" and unit2 == "kilogram":
        return x * 0.45359237

    elif unit1 == "kilogram" and unit2 == "pound":
        return x / 0.45359237

    elif unit1 == "mile" and (unit2 == "feet" or unit2 == "foot"):
        return x * 5280

    elif (unit1 == "feet" or unit1 == "foot") and unit2 == "mile":
        return x / 5280

    else:
        return 'units are not recognized'


def simple_multiply(n=0, m=0):
    """
    returns n times m

    :param n: line n
    :type n: float

    :param m: line m
    :type m: float

    :return: a float value of m * n
    :rtype: float
    """
    print "he is fallen"
    return m * n
