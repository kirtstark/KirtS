"""
Timing performance test for source.main2.Interface
"""

from source.main2 import *
from unittest import TestCase
from test.plugins.ReqTracer import requirements
import time


class TestPerformance(TestCase):

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
    newAnswer3 = 'It is possible there are eight ways'

    @requirements(['#0050', '#0051', '#0052'])
    def test_ask_valid_quadrilateral_question_performance1(self):
        questions = Interface()
        inquiry = 'What type of quadrilateral is 2 2 2 2' + chr(0x3F)
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        print timming
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), result)
        self.assertEqual(qas[-3].strip(), inquiry)

    @requirements(['#0050', '#0051', '#0052'])
    def test_ask_valid_triangle_question_performance(self):
        questions = Interface()
        inquiry = 'What type of triangle is 2.98 2.98 2.98' + chr(0x3F)
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), result)
        self.assertEqual(qas[-3].strip(), inquiry)

    @requirements(['#0050', '#0051', '#0052'])
    def test_ask_for_fibonacci_digit_performance(self):
        questions = Interface()
        inquiry = "What is the 7 digit of fibonacci?"
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)

    @requirements(['#0050', '#0051', '#0052'])
    def test_ask_for_conversion_performance(self):
        questions = Interface()
        inquiry = "Convert 5.6 quarts to liters"
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)

    @requirements(['#0050', '#0051', '#0052'])
    def test_ask_for_conversion_with_unknown_unit_performance(self):
        questions = Interface()
        inquiry = "Convert 8745 tickles to miles"
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)

    @requirements(['#0050', '#0051', '#0052'])
    def test_ask_for_clear_memory_performance(self):
        questions = Interface()
        inquiry = 'Where are my car keys' + chr(0x3F)
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)
        self.assertEqual(result, self.response2)
        questions.opening()
        questions.teach(self.newAnswer1)
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)
        self.assertEqual(result, self.newAnswer1)
        questions.opening()
        inquiry = "Please clear memory"
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)
        questions.opening()
        inquiry = self.keyWord3 + ' are my car keys' + chr(0x3F)
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)
        self.assertEqual(result, self.response2)

    @requirements(['#0050', '#0051', '#0052'])
    def test_ask_for_pi_digit10(self):
        questions = Interface()
        inquiry = "What is the 10 digit of pi?"
        start = time.clock()
        result = questions.ask(inquiry)
        timming = time.clock() - start
        questions.closing()
        with open('QAFile.txt', 'r') as inFile:
            qas = inFile.readlines()
        inFile.close()
        self.assertLess(timming, .05)
        self.assertEqual(qas[-2].strip(), str(result))
        self.assertEqual(qas[-3].strip(), inquiry)
        self.assertEqual(result, 3)