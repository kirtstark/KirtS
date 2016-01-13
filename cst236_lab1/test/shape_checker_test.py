"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from source.shape_checker import get_rectangle_type
from source.shape_checker import get_quadrilateral_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_all_int_invalid1(self):
        result = get_triangle_type(1, -21, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid2(self):
        result = get_triangle_type(71, 1, -81)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid3(self):
        result = get_triangle_type(-1, 1, -81)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid4(self):
        result = get_triangle_type(-1, -945, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid5(self):
        result = get_triangle_type(-1, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid1(self):
        result = get_triangle_type(-1.6, 15.4, 1.7)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid2(self):
        result = get_triangle_type(-1.54, -1.78, 1.74)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid3(self):
        result = get_triangle_type(-1.49, -1.87, -1.64)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid4(self):
        result = get_triangle_type(1.7954, -125.15, 17.2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid5(self):
        result = get_triangle_type(1.157, 11.8, -.258)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(15.89784, 15.89784, 15.89784)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_float(self):
        result = get_triangle_type(87.8754, 87.8755, 87.8756)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix1(self):
        result = get_triangle_type(87.8754, 1, 81)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix2(self):
        result = get_triangle_type(87.8754, 12, 87.8756)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix3(self):
        result = get_triangle_type(72, 87.8755, 87.8756)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix4(self):
        result = get_triangle_type(62, 63, 87.8756)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix5(self):
        result = get_triangle_type(87.8754, 87.8755, 5)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_iscoceles_all_int1(self):
        result = get_triangle_type(3, 2, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int2(self):
        result = get_triangle_type(3, 3, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int3(self):
        result = get_triangle_type(3, 2, 3)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float1(self):
        result = get_triangle_type(3.8, 2.61, 2.61)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float2(self):
        result = get_triangle_type(3.87, 3.87, 2.75)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float3(self):
        result = get_triangle_type(3.49, 2.84, 3.49)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix1(self):
        result = get_triangle_type(3.8, 3.8, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix2(self):
        result = get_triangle_type(3.87, 3, 3.87)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix3(self):
        result = get_triangle_type(3, 2.84, 2.84)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix4(self):
        result = get_triangle_type(3, 3, 2.61)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix5(self):
        result = get_triangle_type(3.87, 2, 2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix6(self):
        result = get_triangle_type(7, 2.84, 7)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_char(self):
        result = get_triangle_type('a', 'b', 'c')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char1(self):
        result = get_triangle_type('a', 'b', 2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char2(self):
        result = get_triangle_type('a', 2, 'c')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char3(self):
        result = get_triangle_type(5, 'b', 'c')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char4(self):
        result = get_triangle_type('a', 2, 7)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char5(self):
        result = get_triangle_type(5, 8, 'c')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char6(self):
        result = get_triangle_type(7, 'b', 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_string(self):
        a = "hello"
        result = get_triangle_type(a, a, a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string1(self):
        a = "hello"
        result = get_triangle_type(7, a, 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string2(self):
        a = "hello"
        result = get_triangle_type(a, 6, 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string3(self):
        a = "hello"
        result = get_triangle_type(7, 6, a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string4(self):
        a = "hello"
        result = get_triangle_type(a, a, 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string5(self):
        a = "hello"
        result = get_triangle_type(7, a, a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string6(self):
        a = "hello"
        result = get_triangle_type(a, 14, a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_float_equals_int(self):
        result = get_triangle_type(1, 1.0, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equalateral_large_int(self):
        result = get_triangle_type(548758458, 548758458, 548758458)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_int(self):
        result = get_triangle_type(548758458, 548758456, 548758457)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_int(self):
        result = get_triangle_type(548758458, 548758457, 548758458)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_large_float(self):
        result = get_triangle_type(548758458156785.2, 548758458156785.2, 548758458156785.2)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_float(self):
        result = get_triangle_type(548758458156785.75, 548758458156786.75, 548758458156784.75)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_float(self):
        result = get_triangle_type(548758458156785.82, 548758458156785.82, 548758458156781.82)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_small_float(self):
        result = get_triangle_type(.0000000001, .0000000001, .0000000001)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_small_float(self):
        result = get_triangle_type(.00000000011, .00000000013, .00000000014)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_small_float(self):
        result = get_triangle_type(.00000000011, .00000000013, .00000000011)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_zero_values(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix1_zero_values(self):
        result = get_triangle_type(2, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix2_zero_values(self):
        result = get_triangle_type(0, 1, 2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix3_zero_values(self):
        result = get_triangle_type(1, 0, 2)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix4_zero_values(self):
        result = get_triangle_type(1, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix5_zero_values(self):
        result = get_triangle_type(0, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix6_zero_values(self):
        result = get_triangle_type(0, 0, 7)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_null_values(self):
        result = get_triangle_type()
        self.assertEqual(result, 'invalid')

    def test_get_triangle_one_null_values(self):
        result = get_triangle_type(12, 7.6)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_two_null_values(self):
        result = get_triangle_type(98.6)
        self.assertEqual(result, 'invalid')

# lists

    def test_get_triangle_equilateral_all_int_list(self):
        a = [1, 1, 1]
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_all_int_invalid1_list(self):
        a = [1, -21, 1]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid2_list(self):
        a = [71, 1, -81]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid3_list(self):
        a = [-1, 1, -81]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid4_list(self):
        a = [-1, -945, 1]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid5_list(self):
        a = [-1, 1, 1]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid1_list(self):
        a = [-1.6, 15.4, 1.7]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid2_list(self):
        a = [-1.54, -1.78, 1.74]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid3_list(self):
        a = [-1.49, -1.87, -1.64]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid4_list(self):
        a = [1.7954, -125.15, 17.2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid5_list(self):
        a = [1.157, 11.8, -.258]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_list(self):
        a = [15.89784, 15.89784, 15.89784]
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int_list(self):
        a = [1, 2, 3]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_float_list(self):
        a = [87.8754, 87.8755, 87.8756]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix1_list(self):
        a = [87.8754, 1, 81]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix2_list(self):
        a = [87.8754, 12, 87.8756]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix3_list(self):
        a = [72, 87.8755, 87.8756]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix4_list(self):
        a = [62, 63, 87.8756]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix5_list(self):
        a = [87.8754, 87.8755, 5]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_iscoceles_all_int1_list(self):
        a = [3, 2, 2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int2_list(self):
        a = [3, 3, 2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int3_list(self):
        a = [3, 2, 3]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float1_list(self):
        a = [3.8, 2.61, 2.61]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float2_list(self):
        a = [3.87, 3.87, 2.75]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float3_list(self):
        a = [3.49, 2.84, 3.49]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix1_list(self):
        a = [3.8, 3.8, 2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix2_list(self):
        a = [3.87, 3, 3.87]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix3_list(self):
        a = [3, 2.84, 2.84]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix4_list(self):
        a = [3, 3, 2.61]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix5_list(self):
        a = [3.87, 2, 2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix6_list(self):
        a = [7, 2.84, 7]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_char_list(self):
        a = ['a', 'b', 'c']
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char1_list(self):
        a = ['a', 'b', 2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char2_list(self):
        a = ['a', 2, 'c']
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char3_list(self):
        a = [5, 'b', 'c']
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char4_list(self):
        a = ['a', 2, 7]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char5_list(self):
        a = [5, 8, 'c']
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char6_list(self):
        a = [7, 'b', 3]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_string_list(self):
        b = "hello"
        a = [b, b, b]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string1_list(self):
        b = "hello"
        a = [7, b, 3]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string2_list(self):
        b = "hello"
        a = [b, 7, 3]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string3_list(self):
        b = "hello"
        a = [7, 28, b]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string4_list(self):
        b = "hello"
        a = [b, b, 3]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string5_list(self):
        b = "hello"
        a = [7, b, b]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string6_list(self):
        b = "hello"
        a = [b, 2, b]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_float_equals_int_list(self):
        a = [1, 1.0, 1]
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equalateral_large_int_list(self):
        a = [548758458, 548758458, 548758458]
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_int_list(self):
        a = [548758458, 548758456, 548758457]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_int_list(self):
        a = [548758458, 548758457, 548758458]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_large_float_list(self):
        a = [548758458156785.2, 548758458156785.2, 548758458156785.2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_float_list(self):
        a = [548758458156785.75, 548758458156786.75, 548758458156784.75]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_float_list(self):
        a = [548758458156785.82, 548758458156785.82, 548758458156781.82]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_small_float_list(self):
        a = [.0000000001, .0000000001, .0000000001]
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_small_float_list(self):
        a = [.00000000011, .00000000013, .00000000014]
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_small_float_list(self):
        a = [.00000000011, .00000000013, .00000000011]
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_zero_values_list(self):
        a = [0, 0, 0]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix1_zero_values_list(self):
        a = [2, 1, 0]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix2_zero_values_list(self):
        a = [0, 1, 2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix3_zero_values_list(self):
        a = [1, 0, 2]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix4_zero_values_list(self):
        a = [1, 0, 0]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix5_zero_values_list(self):
        a = [0, 1, 0]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix6_zero_values_list(self):
        a = [0, 0, 7]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_null_values_list(self):
        a = []
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_one_null_values_list(self):
        a = [2, 9]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_two_null_values_list(self):
        a = [8]
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

# tuples

    def test_get_triangle_equilateral_all_int_tuple(self):
        a = (1, 1, 1)
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_all_int_invalid1_tuple(self):
        a = (1, -21, 1)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid2_tuple(self):
        a = (71, 1, -81)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid3_tuple(self):
        a = (-1, 1, -81)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid4_tuple(self):
        a = (-1, -945, 1)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid5_tuple(self):
        a = (-1, 1, 1)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid1_tuple(self):
        a = (-1.6, 15.4, 1.7)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid2_tuple(self):
        a = (-1.54, -1.78, 1.74)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid3_tuple(self):
        a = (-1.49, -1.87, -1.64)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid4_tuple(self):
        a = (1.7954, -125.15, 17.2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid5_tuple(self):
        a = (1.157, 11.8, -.258)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_tuple(self):
        a = (15.89784, 15.89784, 15.89784)
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int_tuple(self):
        a = (1, 2, 3)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_float_tuple(self):
        a = (87.8754, 87.8755, 87.8756)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix1_tuple(self):
        a = (87.8754, 1, 81)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix2_tuple(self):
        a = (87.8754, 12, 87.8756)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix3_tuple(self):
        a = (72, 87.8755, 87.8756)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix4_tuple(self):
        a = (62, 63, 87.8756)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix5_tuple(self):
        a = (87.8754, 87.8755, 5)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_iscoceles_all_int1_tuple(self):
        a = (3, 2, 2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int2_tuple(self):
        a = (3, 3, 2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int3_tuple(self):
        a = (3, 2, 3)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float1_tuple(self):
        a = (3.8, 2.61, 2.61)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float2_tuple(self):
        a = (3.87, 3.87, 2.75)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float3_tuple(self):
        a = (3.49, 2.84, 3.49)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix1_tuple(self):
        a = (3.8, 3.8, 2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix2_tuple(self):
        a = (3.87, 3, 3.87)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix3_tuple(self):
        a = (3, 2.84, 2.84)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix4_tuple(self):
        a = (3, 3, 2.61)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix5_tuple(self):
        a = (3.87, 2, 2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix6_tuple(self):
        a = (7, 2.84, 7)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_char_tuple(self):
        a = ('a', 'b', 'c')
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char1_tuple(self):
        a = ('a', 'b', 2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char2_tuple(self):
        a = ('a', 2, 'c')
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char3_tuple(self):
        a = (5, 'b', 'c')
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char4_tuple(self):
        a = ('a', 2, 7)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char5_tuple(self):
        a = (5, 8, 'c')
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char6_tuple(self):
        a = (7, 'b', 3)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_string_tuple(self):
        b = "hello"
        a = (b, b, b)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string1_tuple(self):
        b = "hello"
        a = (7, b, 3)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string2_tuple(self):
        b = "hello"
        a = (b, 7, 3)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string3_tuple(self):
        b = "hello"
        a = (7, 28, b)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string4_tuple(self):
        b = "hello"
        a = (b, b, 3)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string5_tuple(self):
        b = "hello"
        a = (7, b, b)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string6_tuple(self):
        b = "hello"
        a = (b, 2, b)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_float_equals_int_tuple(self):
        a = (1, 1.0, 1)
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equalateral_large_int_tuple(self):
        a = (548758458, 548758458, 548758458)
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_int_tuple(self):
        a = (548758458, 548758456, 548758457)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_int_tuple(self):
        a = (548758458, 548758457, 548758458)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_large_float_tuple(self):
        a = (548758458156785.2, 548758458156785.2, 548758458156785.2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_float_tuple(self):
        a = (548758458156785.75, 548758458156786.75, 548758458156784.75)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_float_tuple(self):
        a = (548758458156785.82, 548758458156785.82, 548758458156781.82)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_small_float_tuple(self):
        a = (.0000000001, .0000000001, .0000000001)
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_small_float_tuple(self):
        a = (.00000000011, .00000000013, .00000000014)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_small_float_tuple(self):
        a = (.00000000011, .00000000013, .00000000011)
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_zero_values_tuple(self):
        a = (0, 0, 0)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix1_zero_values_tuple(self):
        a = (2, 1, 0)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix2_zero_values_tuple(self):
        a = (0, 1, 2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix3_zero_values_tuple(self):
        a = (1, 0, 2)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix4_zero_values_tuple(self):
        a = (1, 0, 0)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix5_zero_values_tuple(self):
        a = (0, 1, 0)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix6_zero_values_tuple(self):
        a = (0, 0, 7)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_null_values_tuple(self):
        a = ()
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_one_null_values_tuple(self):
        a = (8, 5.6)
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

# dictionaries

    def test_get_triangle_equilateral_all_int_dictionary(self):
        a = {'one': 1, 'two': 1, 'three': 1}
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equilateral_all_int_invalid1_dictionary(self):
        a = {'one': 1, 'two': -21, 'three': 1}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid2_dictionary(self):
        a = {'one': 71, 'two': 1, 'three': -81}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid3_dictionary(self):
        a = {'one': -1, 'two': 1, 'three': -81}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid4_dictionary(self):
        a = {'one': -1, 'two': -945, 'three': 1}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_int_invalid5_dictionary(self):
        a = {'one': -1, 'two': 1, 'three': 1}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid1_dictionary(self):
        a = {'one': -1.6, 'two': 15.4, 'three': 1.7}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid2_dictionary(self):
        a = {'one': -1.54, 'two': -1.78, 'three': 1.74}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid3_dictionary(self):
        a = {'one': -1.49, 'two': -1.87, 'three': -1.64}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid4_dictionary(self):
        a = {'one': 1.7954, 'two': -125.15, 'three': 17.2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_invalid5_dictionary(self):
        a = {'one': 1.157, 'two': 11.8, 'three': -.258}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_all_float_dictionary(self):
        a = {'one': 15.89784, 'two': 15.89784, 'three': 15.89784}
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int_dictionary(self):
        a = {'one': 1, 'two': 2, 'three': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_float_dictionary(self):
        a = {'one': 87.8754, 'two': 87.8755, 'three': 87.8756}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix1_dictionary(self):
        a = {'one': 87.8754, 'two': 1, 'three': 81}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix2_dictionary(self):
        a = {'one': 87.8754, 'two': 12, 'three': 87.8756}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix3_dictionary(self):
        a = {'one': 72, 'two': 87.8755, 'three': 87.8756}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix4_dictionary(self):
        a = {'one': 62, 'two': 63, 'three': 87.8756}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_scalene_all_mix5_dictionary(self):
        a = {'one': 87.8754, 'two': 87.8755, 'three': 5}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_iscoceles_all_int1_dictionary(self):
        a = {'one': 3, 'two': 2, 'three': 2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int2_dictionary(self):
        a = {'one': 3, 'two': 3, 'three': 2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_int3_dictionary(self):
        a = {'one': 3, 'two': 2, 'three': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float1_dictionary(self):
        a = {'one': 3.8, 'two': 2.61, 'three': 2.61}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float2_dictionary(self):
        a = {'one': 3.87, 'two': 3.87, 'three': 2.75}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_float3_dictionary(self):
        a = {'one': 3.49, 'two': 2.84, 'three': 3.49}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix1_dictionary(self):
        a = {'one': 3.8, 'two': 3.8, 'three': 2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix2_dictionary(self):
        a = {'one': 3.87, 'two': 3, 'three': 3.87}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix3_dictionary(self):
        a = {'one': 3, 'two': 2.84, 'three': 2.84}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix4_dictionary(self):
        a = {'one': 3, 'two': 3, 'three': 2.61}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix5_dictionary(self):
        a = {'one': 3.87, 'two': 2, 'three': 2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_iscoceles_all_mix6_dictionary(self):
        a = {'one': 7, 'two': 2.84, 'three': 7}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_char_dictionary(self):
        a = {'one': 'a', 'two': 'b', 'three': 'c'}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char1_dictionary(self):
        a = {'one': 'a', 'two': 'b', 'three': 2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char2_dictionary(self):
        a = {'one': 'a', 'two': 2, 'three': 'c'}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char3_dictionary(self):
        a = {'one': 5, 'two': 'b', 'three': 'c'}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char4_dictionary(self):
        a = {'one': 'a', 'two': 2, 'three': 7}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char5_dictionary(self):
        a = {'one': 5, 'two': 8, 'three': 'c'}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_char6_dictionary(self):
        a = {'one': 7, 'two': 'b', 'three': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_string_dictionary(self):
        b = "hello"
        a = {'one': b, 'two': b, 'three': b}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string1_dictionary(self):
        b = "hello"
        a = {'one': 7, 'two': b, 'three': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string2_dictionary(self):
        b = "hello"
        a = {'one': b, 'two': 7, 'three': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string3_dictionary(self):
        b = "hello"
        a = {'one': 7, 'two': 28, 'three': b}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string4_dictionary(self):
        b = "hello"
        a = {'one': b, 'two': b, 'three': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string5_dictionary(self):
        b = "hello"
        a = {'one': 7, 'two': b, 'three': b}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix_string6_dictionary(self):
        b = "hello"
        a = {'one': b, 'two': 2, 'three': b}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_float_equals_int_dictionary(self):
        a = {'one': 1, 'two': 1.0, 'three': 1}
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_equalateral_large_int_dictionary(self):
        a = {'one': 548758458, 'two': 548758458, 'three': 548758458}
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_int_dictionary(self):
        a = {'one': 548758458, 'two': 548758456, 'three': 548758457}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_int_dictionary(self):
        a = {'one': 548758458, 'two': 548758457, 'three': 548758458}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_large_float_dictionary(self):
        a = {'one': 548758458156785.2, 'two': 548758458156785.2, 'three': 548758458156785.2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_large_float_dictionary(self):
        a = {'one': 548758458156785.75, 'two': 548758458156786.75, 'three': 548758458156784.75}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_large_float_dictionary(self):
        a = {'one': 548758458156785.82, 'two': 548758458156785.82, 'three': 548758458156781.82}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equalateral_small_float_dictionary(self):
        a = {'one': .0000000001, 'two': .0000000001, 'three': .0000000001}
        result = get_triangle_type(a)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_small_float_dictionary(self):
        a = {'one': .00000000011, 'two': .00000000013, 'three': .00000000014}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_small_float_dictionary(self):
        a = {'one': .00000000011, 'two': .00000000013, 'three': .00000000011}
        result = get_triangle_type(a)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_all_zero_values_dictionary(self):
        a = {'one': 0, 'two': 0, 'three': 0}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix1_zero_values_dictionary(self):
        a = {'one': 2, 'two': 1, 'three': 0}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix2_zero_values_dictionary(self):
        a = {'one': 0, 'two': 1, 'three': 2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix3_zero_values_dictionary(self):
        a = {'one': 1, 'two': 0, 'three': 2}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix4_zero_values_dictionary(self):
        a = {'one': 1, 'two': 0, 'three': 0}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix5_zero_values_dictionary(self):
        a = {'one': 0, 'two': 1, 'three': 0}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_mix6_zero_values_dictionary(self):
        a = {'one': 0, 'two': 0, 'three': 7}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_null_values_dictionary(self):
        a = {}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_one_null_values_dictionary(self):
        a = {'one': 0}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_two_null_values_dictionary(self):
        a = {'one': 0, 'two': 0}
        result = get_triangle_type(a)
        self.assertEqual(result, 'invalid')

# testing for rectangles versus squares

    def test_get_rectangle_square_type_all_int(self):
        result = get_rectangle_type(7, 7, 7, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_type_all_int(self):
        result = get_rectangle_type(7, 15, 7, 15)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_square_type_all_float(self):
        result = get_rectangle_type(7.321, 7.321, 7.321, 7.321)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_type_all_float(self):
        result = get_rectangle_type(7.987, 15.258, 7.987, 15.258)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_square_type_mix1(self):
        result = get_rectangle_type(7.0, 7, 7, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix2(self):
        result = get_rectangle_type(7, 7.0, 7, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix3(self):
        result = get_rectangle_type(7, 7, 7.0, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix4(self):
        result = get_rectangle_type(7, 7, 7, 7.0)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix5(self):
        result = get_rectangle_type(7.0, 7.0, 7, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix6(self):
        result = get_rectangle_type(7.0, 7, 7.0, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix7(self):
        result = get_rectangle_type(7.0, 7, 7, 7.0)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix8(self):
        result = get_rectangle_type(7.0, 7.0, 7.0, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix9(self):
        result = get_rectangle_type(7.0, 7.0, 7, 7.0)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix10(self):
        result = get_rectangle_type(7, 7, 7.0, 7.0)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix11(self):
        result = get_rectangle_type(7, 7.0, 7.0, 7.0)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix12(self):
        result = get_rectangle_type(7, 7.0, 7, 7.0)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix13(self):
        result = get_rectangle_type(7, 7, 7, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_square_type_mix14(self):
        result = get_rectangle_type(7, 7.0, 7.0, 7)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_type_mix1(self):
        result = get_rectangle_type(7.987, 15.258, 7.987, 15.258)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix2(self):
        result = get_rectangle_type(7.987, 15, 7.987, 15.0)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix3(self):
        result = get_rectangle_type(7, 15.258, 7.0, 15.258)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix4(self):
        result = get_rectangle_type(7.0, 15.258, 7, 15.258)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix5(self):
        result = get_rectangle_type(7.987, 15.0, 7.987, 15)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix6(self):
        result = get_rectangle_type(7, 15, 7.0, 15.0)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix7(self):
        result = get_rectangle_type(7, 15.258, 7, 15.258)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix8(self):
        result = get_rectangle_type(7, 15.0, 7.0, 15)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix9(self):
        result = get_rectangle_type(7, 15, 7.0, 15.0)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix10(self):
        result = get_rectangle_type(7, 15, 7, 15.0)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix11(self):
        result = get_rectangle_type(7, 15, 7.0, 15)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix12(self):
        result = get_rectangle_type(7.0, 15.0, 7, 15)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix13(self):
        result = get_rectangle_type(7, 15.0, 7, 15)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_square_type_all_0(self):
        result = get_rectangle_type(0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_all_null(self):
        result = get_rectangle_type()
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_all_0(self):
        result = get_rectangle_type(0, 0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix1_0(self):
        result = get_rectangle_type(8, 0, 8, 0)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix2_0(self):
        result = get_rectangle_type(0, 8, 0, 8)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mismatch1(self):
        result = get_rectangle_type(12, 14, 12, 13)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mismatch2(self):
        result = get_rectangle_type(73, 456, 72, 456)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_mismatch1(self):
        result = get_rectangle_type(957, 951, 951, 951)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_mismatch2(self):
        result = get_rectangle_type(951, 957, 951, 951)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_mismatch3(self):
        result = get_rectangle_type(951, 951, 957, 951)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_mismatch4(self):
        result = get_rectangle_type(951, 951, 951, 957)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_all_char(self):
        a = 'x'
        result = get_rectangle_type(a, a, a, a)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_all_char(self):
        a = 'x'
        b = 'y'
        result = get_rectangle_type(a, b, a, b)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_all_string(self):
        a = 'xyz'
        result = get_rectangle_type(a, a, a, a)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_all_string(self):
        a = 'xyz'
        b = 'zyx'
        result = get_rectangle_type(a, b, a, b)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix1_char(self):
        a = 'x'
        result = get_rectangle_type(a, 12.5, a, 12.5)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix2_char(self):
        a = 'x'
        result = get_rectangle_type(12.5, a, 12.5, a)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix1_string(self):
        a = 'xyz'
        result = get_rectangle_type(a, 12.5, a, 12.5)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix2_string(self):
        a = 'xyz'
        result = get_rectangle_type(12.5, a, 12.5, a)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_all_negative(self):
        result = get_rectangle_type(-7, -7, -7, -7)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix1_negative(self):
        result = get_rectangle_type(-7, 4, -7, 4)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_rectangle_type_mix2_negative(self):
        result = get_rectangle_type(4, -7, 4, -7)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_square_type_all_large_int(self):
        a = 0xfffffff
        result = get_rectangle_type(a, a, a, a)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_type_mix1_large_int(self):
        a = 0xfffffff
        result = get_rectangle_type(a, 4, a, 4)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix2_large_int(self):
        a = 0xfffffff
        result = get_rectangle_type(4, a, 4, a)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_square_type_all_large_float(self):
        a = 0xfffffff + .2574
        result = get_rectangle_type(a, a, a, a)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_type_mix1_large_float(self):
        a = 0xfffffff + .257
        result = get_rectangle_type(a, 4, a, 4)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix2_large_float(self):
        a = 0xfffffff + .258
        result = get_rectangle_type(4, a, 4, a)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_square_type_all_small_float(self):
        a = .0000000001
        result = get_rectangle_type(a, a, a, a)
        self.assertEqual(result, 'square')

    def test_get_rectangle_rectangle_type_mix1_small_float(self):
        a = .0000000001
        result = get_rectangle_type(a, 4, a, 4)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_rectangle_type_mix2_small_float(self):
        a = .0000000001
        result = get_rectangle_type(4, a, 4, a)
        self.assertEqual(result, 'rectangle')

# testing for quadrilateral type

    def test_get_quadrilateral_type_rectangle_all_int(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_type_square_all_int(self):
        result = get_quadrilateral_type(7, 7, 7, 7, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_type_square_all_int_negative_sides(self):
        result = get_quadrilateral_type(-7, -7, -7, -7, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_square_all_long_negative_sides(self):
        result = get_quadrilateral_type(-7.24, -7.24, -7.24, -7.24, 90, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_square_all_int_negative_angles(self):
        result = get_quadrilateral_type(7, 7, 7, 7, -90, -90, -90, -90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_rectangle_large_angles1(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 270, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_rectangle_large_angles2(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90, 270, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_rectangle_large_angles3(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90, 90, 270, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_rectangle_large_angles4(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90, 90, 90, 270)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_rectangle_all_long(self):
        result = get_quadrilateral_type(1.2, 7.1, 1.2, 7.1, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_type_rectangle_mix1(self):
        result = get_quadrilateral_type(1, 7.1, 1, 7.1, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_type_rectangle_mix2(self):
        result = get_quadrilateral_type(1.2, 7, 1.2, 7, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_type_square_all_long(self):
        result = get_quadrilateral_type(7.896, 7.896, 7.896, 7.896, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_type_rectangle_too_long(self):
        result = get_quadrilateral_type(1, 7, 1.1, 7, 90, 90, 90, 90)
        self.assertEqual(result, 'disconnected')

    def test_get_quadrilateral_type_square_too_long(self):
        result = get_quadrilateral_type(7, 7, 7.1, 7, 90, 90, 90, 90)
        self.assertEqual(result, 'disconnected')

    def test_get_quadrilateral_type_square_too_short(self):
        result = get_quadrilateral_type(6.69, 7, 7, 7, 90, 90, 90, 90)
        self.assertEqual(result, 'disconnected')

    def test_get_quadrilateral_type_square_angle_too_large(self):
        result = get_quadrilateral_type(7, 7, 7, 7, 90.3, 90, 90, 90)
        self.assertEqual(result, 'disconnected')

    def test_get_quadrilateral_type_rectangle_angle_too_small(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90, 90, 89.7, 90)
        self.assertEqual(result, 'disconnected')

    def test_get_quadrilateral_type_rhombus_all_int(self):
        result = get_quadrilateral_type(7, 7, 7, 7, 70, 110, 70, 110)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_type_rhombus_all_long(self):
        result = get_quadrilateral_type(7.31, 7.31, 7.31, 7.31, 110.25, 69.75, 110.25, 69.75)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_type_char_all(self):
        a = 'a'
        result = get_quadrilateral_type(a, a, a, a, a, a, a, a)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix1(self):
         a = 'a'
         result = get_quadrilateral_type(a, 7, 7, 7, 70, 110, 70, 110)
         self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix2(self):
        a = 'a'
        result = get_quadrilateral_type(7, a, 7, 7, 70, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix3(self):
        a = 'a'
        result = get_quadrilateral_type(7, 7, a, 7, 70, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix4(self):
        a = 'a'
        result = get_quadrilateral_type(7, 7, 7, a, 70, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix5(self):
        a = 'a'
        result = get_quadrilateral_type(7, 7, 7, 7, a, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix6(self):
        a = 'a'
        result = get_quadrilateral_type(7, 7, 7, 7, 70, a, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix7(self):
        a = 'a'
        result = get_quadrilateral_type(7, 7, 7, 7, 70, 110, a, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_char_mix8(self):
        a = 'a'
        result = get_quadrilateral_type(7, 7, 7, 7, 70, 110, 70, a)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_all(self):
        a = 'abc'
        result = get_quadrilateral_type(a, a, a, a, a, a, a, a)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix1(self):
         a = 'abc'
         result = get_quadrilateral_type(a, 7, 7, 7, 70, 110, 70, 110)
         self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix2(self):
        a = 'abc'
        result = get_quadrilateral_type(7, a, 7, 7, 70, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix3(self):
        a = 'abc'
        result = get_quadrilateral_type(7, 7, a, 7, 70, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix4(self):
        a = 'abc'
        result = get_quadrilateral_type(7, 7, 7, a, 70, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix5(self):
        a = 'abc'
        result = get_quadrilateral_type(7, 7, 7, 7, a, 110, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix6(self):
        a = 'abc'
        result = get_quadrilateral_type(7, 7, 7, 7, 70, a, 70, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix7(self):
        a = 'abc'
        result = get_quadrilateral_type(7, 7, 7, 7, 70, 110, a, 110)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_string_mix8(self):
        a = 'abc'
        result = get_quadrilateral_type(7, 7, 7, 7, 70, 110, 70, a)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_none_all_int(self):
        result = get_quadrilateral_type(50, 10, 35.85786, 10, 45, 45, 135, 135)
        self.assertEqual(result, 'none')

    def test_get_quadrilateral_type_null_all(self):
        result = get_quadrilateral_type()
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_null_value1(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_null_value2(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_null_value3(self):
        result = get_quadrilateral_type(1, 7, 1, 7, 90)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_null_value4(self):
        result = get_quadrilateral_type(1, 7, 1, 7)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_null_value5(self):
        result = get_quadrilateral_type(1, 7, 1, 7)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_null_value6(self):
        result = get_quadrilateral_type(1, 7)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_null_value7(self):
        result = get_quadrilateral_type(1)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_type_square_large_long(self):
        a = 0xfffff + .0447
        result = get_quadrilateral_type(a, a, a, a, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_type_square_large_int(self):
        result = get_quadrilateral_type(0xfffff, 0xfffff, 0xfffff, 0xfffff, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_type_square_small_long(self):
        a = .000000001
        result = get_quadrilateral_type(a, a, a, a, 90, 90, 90, 90)
        self.assertEqual(result, 'square')



