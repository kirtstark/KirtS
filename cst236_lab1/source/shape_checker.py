"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""

from math import*

def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """

    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


# The following example code determines if a set of 4 sides of a rectangle forms a square or just a rectangle

def get_rectangle_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given rectangle is a square or only a rectangle

    :param a: line a
    :type a: float or int

    :param b: line b
    :type b: float or int

    :param c: line c
    :type c: float or int

    :param d: line d
    :type d: float or int

    :return: "square", "rectangle" or "invalid"
    :rtype: str
    """

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and
            isinstance(d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        return "square"

    elif a == c and b == d:
        return "rectangle"

    else:
        return "invalid"

# The following example code determines if a set of 4 sides and 4 angles form a square, rectangle, rhombus,
# or if the sides are disconnected, or none if it is a quadrilateral that is not one of these shapes


def get_quadrilateral_type(a=0, b=0, c=0, d=0, angle_d_a=0, angle_a_b=0, angle_b_c=0, angle_c_d=0):
    """
    Determine if the given rectangle is a square or only a rectangle

    :param a: line a
    :type a: float or int

    :param b: line b
    :type b: float or int

    :param c: line c
    :type c: float or int

    :param d: line d
    :type d: float or int

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

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and
            isinstance(d, (int, float)) and isinstance(angle_d_a, (int, float)) and
            isinstance(angle_a_b, (int, float)) and isinstance(angle_b_c, (int, float)) and
            isinstance(angle_c_d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0 or angle_a_b <= 0 or angle_b_c <= 0 or angle_c_d <= 0 or angle_d_a <= 0:
        return "invalid"

    if angle_a_b >= 180 or angle_b_c >= 180 or angle_c_d >= 180 or angle_d_a >= 180:
        return "invalid"

    # the sum of the angles are compared in a range from 359.9 to 360.1
    #    to account for addition rounding or measurement errors
    #    otherwise, we would compare directly to 360 degrees
    if (angle_a_b + angle_b_c + angle_c_d + angle_d_a) > 360.1 or \
            (angle_a_b + angle_b_c + angle_c_d + angle_d_a) < 359.9:
        return "disconnected"

    # check to see that all sides are correct length, using trigonometry
    diag = sqrt(a**2 + d**2 - 2*a*d*cos(radians(angle_d_a)))

    cosangle = (diag**2 + a**2 - d**2)/(2*diag*a)
    if cosangle > 1 or cosangle < -1:
        return "disconnected"
    tempangle = angle_a_b - degrees(acos(cosangle))
    if tempangle <= 0:
        return "disconnected"
    c2 = diag*sin(radians(tempangle))/sin(radians(angle_b_c))

    # using a range to account for math rounding errors
    if c >= (c2 + .05) or c <= (c2 - .05):
        return "disconnected"

    if angle_a_b == 90:
        if a == b and b == c and c == d:
            return "square"
        elif a == c and b == d:
            return "rectangle"
    elif a == b and b == c and c == d:
        return "rhombus"

    return "none"
