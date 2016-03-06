"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral,
 scalene or iscoceles
"""

# disabling for too many arguments in method,
# as large number of arguments are needed
# to satisfy requirements
# diabling "int has no keys member" for line
# 38 and "int has no values member" for line
# 40 as a is clearly marked as a possible
# tuple or dictionary, not just as an int
# pylint: disable=R0913, E1101

from math import sin, cos, radians, acos, sqrt, degrees

def get_triangle_type(a_side=0, b_side=0, c_side=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a_side: line a_side
    :type a_side: float or int or tuple or list or dict

    :param b_side: line b_side
    :type b_side: float

    :param c_side: line c_side
    :type c_side: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """

    if isinstance(a_side, (tuple, list)) and len(a_side) == 3:
        c_side = a_side[2]
        b_side = a_side[1]
        a_side = a_side[0]

    if isinstance(a_side, dict) and len(a_side.keys()) == 3:
        values = []
        for value in a_side.values():
            values.append(value)
        a_side = values[0]
        b_side = values[1]
        c_side = values[2]

    if not (isinstance(a_side, (int, float)) and isinstance(b_side, (int, float)) and
            isinstance(c_side, (int, float))):
        return "invalid"

    if a_side <= 0 or b_side <= 0 or c_side <= 0:
        return "invalid"

    if a_side == b_side and b_side == c_side:
        return "equilateral"

    elif a_side == b_side or a_side == c_side or b_side == c_side:
        return "isosceles"
    else:
        return "scalene"


# The following example code determines if a set of 4 sides of a rectangle forms a square or
#  just a rectangle

def get_rectangle_type(a_side=0, b_side=0, c_side=0, d_side=0):
    """
    Determine if the given rectangle is a square or only a rectangle

    :param a_side: line a_side
    :type a_side: float or int

    :param b_side: line b_side
    :type b_side: float or int

    :param c_side: line c_side
    :type c_side: float or int

    :param d_side: line d_side
    :type d_side: float or int

    :return: "square", "rectangle" or "invalid"
    :rtype: str
    """

    if not (isinstance(a_side, (int, float)) and isinstance(b_side, (int, float)) and
            isinstance(c_side, (int, float)) and isinstance(d_side, (int, float))):
        return "invalid"

    if a_side <= 0 or b_side <= 0 or c_side <= 0 or d_side <= 0:
        return "invalid"

    if a_side == b_side and b_side == c_side and c_side == d_side:
        return "square"

    elif a_side == c_side and b_side == d_side:
        return "rectangle"

    else:
        return "invalid"

# The following example code determines if a set of 4 sides and 4 angles form a square, rectangle,
# rhombus,
# or if the sides are disconnected, or none if it is a quadrilateral that is not one of these shapes


def get_quadrilateral_type(a_side=0, b_side=0, c_side=0, d_side=0, angle_d_a=0,
                           angle_a_b=0, angle_b_c=0, angle_c_d=0):
    """
    Determine if the given rectangle is a square or only a rectangle

    :param a_side: line a_side
    :type a_side: float or int

    :param b_side: line b_side
    :type b_side: float or int

    :param c_side: line c_side
    :type c_side: float or int

    :param d_side: line d_side
    :type d_side: float or int

    :param angle_d_a: line angle_d_a
    :type angle_d_a: float or int

    :param angle_a_b: line angle_a_b
    :type angle_a_b: float or int

    :param angle_b_c: line angle_b_c
    :type angle_b_c: float or int

    :param angle_c_d: line angle_c_d
    :type angle_c_d: float or int

    :return: "square", "rectangle", "rhombus", "disconnected", "none" or "invalid"
    :rtype: str
    """

    result = "none"

    if not (isinstance(a_side, (int, float)) and isinstance(b_side, (int, float)) and
            isinstance(c_side, (int, float)) and
            isinstance(d_side, (int, float)) and isinstance(angle_d_a, (int, float)) and
            isinstance(angle_a_b, (int, float)) and isinstance(angle_b_c, (int, float)) and
            isinstance(angle_c_d, (int, float))):
        result = "invalid"

    elif a_side <= 0 or b_side <= 0 or c_side <= 0 or d_side <= 0:
        result = "invalid"

    elif angle_a_b <= 0 or angle_b_c <= 0 or angle_c_d <= 0 or angle_d_a <= 0:
        result = "invalid"

    elif angle_a_b >= 180 or angle_b_c >= 180 or angle_c_d >= 180 or angle_d_a >= 180:
        result = "invalid"

    # the sum of the angles are compared in a range from 359.9 to 360.1
    #    to account for addition rounding or measurement errors
    #    otherwise, we would compare directly to 360 degrees
    elif (angle_a_b + angle_b_c + angle_c_d + angle_d_a) > 360.1 or \
            (angle_a_b + angle_b_c + angle_c_d + angle_d_a) < 359.9:
        result = "disconnected"

    if result != "none":
        return result

    # check to see that all sides are correct length, using trigonometry
    diag = sqrt(a_side**2 + d_side**2 - 2*a_side*d_side*cos(radians(angle_d_a)))

    cosangle = (diag**2 + a_side**2 - d_side**2)/(2*diag*a_side)
    tempangle = angle_a_b - degrees(acos(cosangle))
    c_2 = diag*sin(radians(tempangle))/sin(radians(angle_b_c))

    # using a range to account for math rounding errors
    if c_side >= (c_2 + .05) or c_side <= (c_2 - .05):
        result = "disconnected"

    elif angle_a_b == 90:
        if a_side == b_side and b_side == c_side and c_side == d_side:
            result = "square"
        elif a_side == c_side and b_side == d_side:
            result = "rectangle"
    elif a_side == b_side and b_side == c_side and c_side == d_side:
        result = "rhombus"

    return result
