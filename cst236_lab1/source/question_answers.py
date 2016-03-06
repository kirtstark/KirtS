"""
:mod:`source.source1` -- Example source code
============================================

The following example code provides story question answers
"""

# disabling for num - unused variable,
# only using num as a placeholder to
# allow "for" keyword to cycle through
# range in line 41
# pylint: disable=W0612

import math
import getpass
from source.question_answer import Reason

def get_fibonacci(position=0):
    """
    returns the nth number in the fibonacci sequence

    :param position: line position
    :type position: int, float

    :return: fibonacci number
    :rtype: int
    """

    if position < 0:
        return 'I cannot process a negative number'

    if position == 0:
        return 0

    if position == 1 or position == 2:
        return 1

    start_1 = 1
    start_2 = 1

    next_1 = int(round(position))
    for num in range(2, next_1):
        follow = start_1 + start_2
        start_1 = start_2
        start_2 = follow

    return follow


def get_some_pi(piece=0):
    """
    returns the nth number in pi, up to the 13th digit

    :param piece: line a
    :type piece: int, float

    :return: piece-th digit number
    :rtype: int
    """
    if piece <= 0:
        return 'The number must be greater than zero'

    elif piece > 12:
        return 'taken too far'

    else:
        return int(str(math.pi).replace('.', '')[int(round(piece)) - 1])


def get_the_door():
    """
    returns a string response with the username taken from the open account

    :param na
    :type na

    :return: a sentence response that includes the system username
    :rtype: str
    """

    return 'I\'m afraid I can\'t do that ' + getpass.getuser()

def convert_unit_to_unit(question):
    """
    returns a number value of the converted unit

    :param question: line question
    :type begin_value: string

    :return: a float value of a number converted from one unit to another, or error code
    :rtype: float, string
    """

    words = question.split(' ')

    if words.__len__() != 5:
        return "incorrect number of words in conversion question"

    try:
        begin_value = float(words[1].strip(' '))
    except ValueError:
        return "error in number value"

    unit1 = words[2].strip(' ')
    unit2 = words[4].strip(' ')

    if unit1 == "inches":
        unit1 = "inch"

    if unit2 == "inches":
        unit2 = "inch"

    if unit1[-1] == 's' and unit1.__len__ > 1:
        unit1 = str(unit1[0:-1])

    if unit2[-1] == 's' and unit2.__len__ > 1:
        unit2 = str(unit2[0:-1])

    conversions = {"centimeter to inch": 0.39370079, "inch to centimeter": 1/0.39370079,
                   "quart to liter": 0.94635295, "liter to quart": 1/0.94635295,
                   "pound to kilogram": 0.45359237, "kilogram to pound": 1/0.45359237,
                   "mile to feet": 5280, "feet to mile": 0.00018939393,
                   "mile to foot": 5280, "foot to mile": 0.00018939393}
    converts_combined = unit1 + ' to ' + unit2

    for convert in conversions:
        if convert == converts_combined:
            return conversions[convert] * begin_value

    if unit1 == "fahrenheit" and unit2 == "centigrade":
        return (begin_value - 32) * 5 / 9

    elif unit1 == "centigrade" and unit2 == "fahrenheit":
        return begin_value * 9 / 5 + 32

    else:
        return 'units are not recognized'


def simple_multiply(mult_a=0, mult_b=0):
    """
    returns mult_a times mult_b

    :param mult_a: line mult_a
    :type mult_a: float

    :param mult_b: line mult_b
    :type mult_b: float

    :return: a float value of m * n
    :rtype: float
    """
    return mult_a * mult_b


def cube_of_number(in_value=0):
    """
    returns the cube of the number

    :param x: line x
    :type x: float

    :return: a float value of the cube of the number
    :rtype: float
    """
    return in_value * in_value * in_value

def divide_evenly(denominator=0, numerator=0):
    """
    returns the even divisor

    :param denominator: line denominator
    :type denominator: float

    :param numerator: line numerator
    :type numerator: float

    :return: a float value of the evenly divided number numerator divided by denominator
    :rtype: float
    """

    if denominator == 0:
        return "division by zero is not possible!"

    elif numerator == 0:
        return 0

    else:
        divided = numerator/denominator
        if divided > 0:
            return math.floor(divided)
        else:
            return math.ceil(divided)

def paycheck(mult_1=0, mult_2=0, add_1=0):
    """
    returns the multiplication of x and y added to z

    :param mult_1: line mult_1
    :type mult_1: float

    :param mult_2: line mult_2
    :type mult_2: float

    :param add_1: line add_1
    :type add_1: float

    :return: a float value of x times y plus z
    :rtype: float
    """

    return mult_1 * mult_2 + add_1

def density_check(material='', vol=0):
    """
    returns the mass of the given material at the given volume (d*v)
    :param material: string

    :param vol: float

    :return: float
    """

    densities = {'helium': .179, 'aerographite': .2, 'cork': 240, 'pine': 373, 'lithium': 535,
                 'oak': 710, 'potassium': 860, 'sodium': 970, 'water': 1000, 'plastic': 1175,
                 'magnesium': 1740, 'beryllium': 1850, 'silicon': 2330, 'aluminium': 2700,
                 'diamond': 3500, 'titanium': 4540, 'zine': 7000}

    lower_material = material.lower()

    for matter in densities:
        if lower_material == matter:
            return vol * densities[matter]

    return "unfamiliar material"

def struggle_reason():
    """
    returns a string offering a reason why these labs are so hard. chosen randomly.
    :return: string
    """

    reason = Reason()
    return reason.get_reason()

