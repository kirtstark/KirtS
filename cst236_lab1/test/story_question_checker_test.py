"""
Test for source.main2.Interface
"""

import math
from source.main2 import *
from unittest import TestCase
from test.plugins.ReqTracer import story
import time
import getpass


class TestStoryQuestionAnswer(TestCase):

    response1 = "Was that a question?"
    response2 = "I don't know, please provide the answer"
    response3 = "Please ask a question first"
    response4 = "I don\'t know about that. I was taught differently"
    keyWord1 = "How"
    keyWord2 = "What"
    keyWord3 = "Where"
    keyWord4 = "Why"
    keyWord5 = "Who"
    question1 = 'What type of triangle is '
    question2 = 'What type of quadrilateral is '
    newAnswer1 = 'Your keys are under the sofa'
    newAnswer2 = 'At least seven ways'
    newAnswer3 = 'It is possible threre are eigth ways'

#   all we have is time
    @story(['What time is it?'])
    def test_ask_for_time(self):
        r = math.pi
        questions = Interface()
        inquiry = "What time is it?"
        localtime1 = time.asctime()
        result = questions.ask(inquiry)
        localtime2 = time.asctime()
        if result == localtime1 or result == localtime2:
            matches = True
        else:
            matches = False
        self.assertTrue(matches)

#   fibonacci tests
    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit(self):
        questions = Interface()
        inquiry = "What is the 0 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 0)

    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit1(self):
        questions = Interface()
        inquiry = "What is the 1 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 1)

    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit2(self):
        questions = Interface()
        inquiry = "What is the 2 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 1)

    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit3(self):
        questions = Interface()
        inquiry = "What is the 3 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 2)

    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit4(self):
        questions = Interface()
        inquiry = "What is the 4 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 3)

    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit5(self):
        questions = Interface()
        inquiry = "What is the 5 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 5)

    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit6(self):
        questions = Interface()
        inquiry = "What is the 6 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 8)

    @story(['What is the n digit of fibonacci?'])
    def test_ask_for_fibonacci_digit7(self):
        questions = Interface()
        inquiry = "What is the 7 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 13)

#   pi anyone?
    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit1(self):
        questions = Interface()
        inquiry = "What is the 1 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 3)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit2(self):
        questions = Interface()
        inquiry = "What is the 2 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 1)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit3(self):
        questions = Interface()
        inquiry = "What is the 3 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 4)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit4(self):
        questions = Interface()
        inquiry = "What is the 4 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 1)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit5(self):
        questions = Interface()
        inquiry = "What is the 5 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 5)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit6(self):
        questions = Interface()
        inquiry = "What is the 6 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 9)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit7(self):
        questions = Interface()
        inquiry = "What is the 7 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 2)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit8(self):
        questions = Interface()
        inquiry = "What is the 8 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 6)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit9(self):
        questions = Interface()
        inquiry = "What is the 9 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 5)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit10(self):
        questions = Interface()
        inquiry = "What is the 10 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 3)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit11(self):
        questions = Interface()
        inquiry = "What is the 11 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 5)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit12(self):
        questions = Interface()
        inquiry = "What is the 12 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 9)

    @story(['What is the n digit of pi?'])
    def test_ask_for_pi_digit13(self):
        questions = Interface()
        inquiry = "What is the 13 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 'taken too far')

#   I forgot, and so should you!

    @story(['Please clear memory'])
    def test_ask_for_clear_memory(self):
        questions = Interface()
        inquiry = self.keyWord3 + ' are my car keys' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response2)
        questions.teach(self.newAnswer1)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.newAnswer1)
        inquiry = "Please clear memory"
        result = questions.ask(inquiry)
        print result
        inquiry = self.keyWord3 + ' are my car keys' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response2)

#   get the door
    @story(['Open the door hal'])
    def test_ask_for_open_door(self):
        questions = Interface()
        inquiry = 'Open the door hal'
        result = questions.ask(inquiry)
        username = getpass.getuser()
        print username
        response = 'I\'m afraid I can\'t do that ' + username
        self.assertEqual(result, response)

#   inspiring conversion stories
    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion1(self):
        questions = Interface()
        inquiry = "Convert 3.2 centimeters to inches"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 1.25984, 4)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion2(self):
        questions = Interface()
        inquiry = "Convert 4.8 inches to centimeters"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 12.192, 2)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion3(self):
        questions = Interface()
        inquiry = "Convert 5.6 quarts to liters"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 5.29957, 4)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion4(self):
        questions = Interface()
        inquiry = "Convert 8.2 liters to quarts"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 8.664847, 4)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion5(self):
        questions = Interface()
        inquiry = "Convert 27 fahrenheit to centigrade"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, -2.7777777, 5)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion6(self):
        questions = Interface()
        inquiry = "Convert 38 centigrade to fahrenheit"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 100.4, 1)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion7(self):
        questions = Interface()
        inquiry = "Convert 72.9 pounds to kilograms"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 33.06685, 4)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion8(self):
        questions = Interface()
        inquiry = "Convert 11.2 kilograms to pounds"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 24.69179, 4)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion9(self):
        questions = Interface()
        inquiry = "Convert 45 miles to feet"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 237600.88583, -2)

    @story(['Convert <number> <units> to <units>', 'at least 10 different units'])
    def test_ask_for_conversion10(self):
        questions = Interface()
        inquiry = "Convert 8745 feet to miles"
        result = questions.ask(inquiry)
        print result
        try:
            result = float(result)
        except:
            result = 0
        self.assertAlmostEqual(result, 1.65624, 4)

    @story(['Why did the chicken cross the road?'])
    def test_ask_for_chicken(self):
        r = math.pi
        questions = Interface()
        inquiry = "Why did the chicken cross the road?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 'To prove to the armadillo that it can be done')

#   programmer created stories
    @story(['What is the <negative number> digit of fibonacci?'])
    def test_ask_for_fibonacci_negative_digit(self):
        questions = Interface()
        inquiry = "What is the -4 digit of fibonacci?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 'I cannot process a negative number')

    @story(['What is the <negative number or zero> digit of pi?'])
    def test_ask_for_pi_zero_digit(self):
        questions = Interface()
        inquiry = "What is the 0 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 'The number must be greater than zero')

    @story(['What is the <negative number or zero> digit of pi?'])
    def test_ask_for_pi_negative_digit(self):
        questions = Interface()
        inquiry = "What is the -11 digit of pi?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 'The number must be greater than zero')

    @story(['What is n multiplied by m?'])
    def test_ask_for_n_time_m1(self):
        questions = Interface()
        inquiry = "What is 4 multiplied by 6.2?"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            print result
        self.assertEqual(result, 24.8)

    @story(['What is n multiplied by m?'])
    def test_ask_for_n_time_m2(self):
        questions = Interface()
        inquiry = "What is 8 multiplied by 6?"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            print result
        self.assertEqual(result, 48)

    @story(['What is n multiplied by m?'])
    def test_ask_for_n_time_m3(self):
        questions = Interface()
        inquiry = "What is 4.5 multiplied by 7.6?"
        result = questions.ask(inquiry)
        try:
            result = float(result)
        except:
            print result
        self.assertEqual(result, (4.5*7.6))

    @story(['What student really deserves an A?'])
    def test_ask_for_A(self):
        questions = Interface()
        inquiry = "What student really deserves an A?"
        result = questions.ask(inquiry)
        self.assertEqual(result, 'Kirt Stark does!')