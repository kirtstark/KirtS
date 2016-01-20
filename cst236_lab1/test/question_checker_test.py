"""
Test for source.main2.Interface
"""

from source.main2 import *
from unittest import TestCase
from test.plugins.ReqTracer import requirements


class TestQuestionAnswer(TestCase):

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

    @requirements(['#0006'])
    def test_ask_correct_type1(self):
        questions = Interface()
        inquiry = "any given question"
        result = questions.ask(inquiry)
        self.assertNotEqual(result, '')

    @requirements(['#0006', '#0007', '#0009'])
    def test_ask_correct_type2(self):
        questions = Interface()
        inquiry = self.keyWord1 + ' ' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertNotEqual(result, self.response1)
        self.assertNotEqual(result, '')

    @requirements(['#0006', '#0007', '#0009'])
    def test_ask_correct_type3(self):
        questions = Interface()
        inquiry = self.keyWord2 + ' ' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertNotEqual(result, self.response1)
        self.assertNotEqual(result, '')

    @requirements(['#0006', '#0007', '#0009'])
    def test_ask_correct_type4(self):
        questions = Interface()
        inquiry = self.keyWord3 + ' ' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertNotEqual(result, self.response1)
        self.assertNotEqual(result, '')

    @requirements(['#0006', '#0007', '#0009'])
    def test_ask_correct_type5(self):
        questions = Interface()
        inquiry = self.keyWord4 + ' ' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertNotEqual(result, self.response1)
        self.assertNotEqual(result, '')

    @requirements(['#0006', '#0007', '#0009'])
    def test_ask_correct_type6(self):
        questions = Interface()
        inquiry = self.keyWord5 + ' ' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertNotEqual(result, self.response1)
        self.assertNotEqual(result, '')

    @requirements(['#0008'])
    def test_ask_no_leading_keyword(self):
        questions = Interface()
        inquiry = 'is this a question' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0009'])
    def test_ask_no_question_mark1(self):
        questions = Interface()
        inquiry = self.keyWord1 + 'is this a question'
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0009'])
    def test_ask_no_question_mark2(self):
        questions = Interface()
        inquiry = self.keyWord2 + 'is this a question'
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0009'])
    def test_ask_no_question_mark3(self):
        questions = Interface()
        inquiry = self.keyWord3 + 'is this a question'
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0009'])
    def test_ask_no_question_mark4(self):
        questions = Interface()
        inquiry = self.keyWord4 + 'is this a question'
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0009'])
    def test_ask_no_question_mark5(self):
        questions = Interface()
        inquiry = self.keyWord5 + 'is this a question'
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0007'])
    def test_ask_lowercase1(self):
        questions = Interface()
        inquiry = 'what' + ' is this a question' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0007'])
    def test_ask_lowercase2(self):
        questions = Interface()
        inquiry = 'how' + ' is this a question' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0007'])
    def test_ask_lowercase3(self):
        questions = Interface()
        inquiry = 'where' + ' is this a question' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0007'])
    def test_ask_lowercase4(self):
        questions = Interface()
        inquiry = 'why' + ' is this a question' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0007'])
    def test_ask_lowercase5(self):
        questions = Interface()
        inquiry = 'who' + ' is this a question' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0010'])
    def test_ask_no_space1(self):
        questions = Interface()
        inquiry = self.keyWord1 + 'no space here' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0010'])
    def test_ask_no_space2(self):
        questions = Interface()
        inquiry = self.keyWord2 + 'no space here' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0010'])
    def test_ask_no_space3(self):
        questions = Interface()
        inquiry = self.keyWord3 + 'no space here' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0010'])
    def test_ask_no_space4(self):
        questions = Interface()
        inquiry = self.keyWord4 + 'no space here' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0010'])
    def test_ask_no_space5(self):
        questions = Interface()
        inquiry = self.keyWord5 + 'no space here' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response1)

    @requirements(['#0014'])
    def test_ask_no_valid_answer(self):
        questions = Interface()
        inquiry = self.keyWord2 + ' color do smurfs turn when you choke them' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertNotEqual(result, '')

    @requirements(['#0014'])
    def test_ask_question_with_no_answer(self):
        questions = Interface()
        inquiry = self.keyWord3 + ' are my car keys' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response2)

    @requirements(['#0015', '#0016'])
    def test_ask_question_with_no_answer(self):
        questions = Interface()
        inquiry = self.keyWord3 + ' are my car keys' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response2)
        result = questions.teach(self.newAnswer1)
        self.assertEqual(result, None)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.newAnswer1)

    @requirements(['#0015', '#0016', '#0011', '#0018', '#0019', '#0020', '#0021'])
    def test_ask_question_with_no_answer2(self):
        questions = Interface()
        inquiry = self.keyWord1 + ' many possible ways are there to skin a really fat cat' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response2)
        result = questions.teach(self.newAnswer2)
        self.assertEqual(result, None)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.newAnswer2)
        result = questions.teach(self.newAnswer1)
        self.assertEqual(result, self.response4)
        result = questions.correct(self.newAnswer3)
        self.assertEqual(result, None)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.newAnswer3)
#           90% correct still
        inquiry = self.keyWord1 + ' many possible ways are there to skin a very fat cat' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.newAnswer3)
#           80% correct still
        inquiry = self.keyWord1 + ' many possible methods are there to skin a very fat cat' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, self.response2)

    @requirements(['#0021'])
    def test_correct_answer_for_no_question(self):
        questions = Interface()
        result = questions.correct(self.newAnswer1)
        self.assertEqual(result, self.response3)

    @requirements(['#0017'])
    def test_provide_answer_with_no_question(self):
        questions = Interface()
        result = questions.teach(self.newAnswer2)
        self.assertEqual(result, self.response3)

    @requirements(['#0012', '#0013'])
    def test_ask_valid_triangle_question1(self):
        questions = Interface()
        inquiry = 'What type of triangle is 2 2 2' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0012', '#0013'])
    def test_ask_valid_triangle_question2(self):
        questions = Interface()
        inquiry = 'What type of triangle is 2 3 2' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0012', '#0013'])
    def test_ask_valid_triangle_question3(self):
        questions = Interface()
        inquiry = 'What type of triangle is 5 3 2' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'scalene')

    @requirements(['#0012', '#0013'])
    def test_ask_valid_triangle_question4(self):
        questions = Interface()
        inquiry = 'What type of triangle is 2.98 2.98 2.98' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0012', '#0013'])
    def test_ask_valid_triangle_question5(self):
        questions = Interface()
        inquiry = 'What type of triangle is 2.5 3.845 2.5' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0012', '#0013'])
    def test_ask_valid_triangle_question6(self):
        questions = Interface()
        inquiry = 'What type of triangle is 5.8 3.4 2.627' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'scalene')

    @requirements(['#0012', '#0013'])
    def test_ask_valid_quadrilateral_question1(self):
        questions = Interface()
        inquiry = 'What type of quadrilateral is 2 2 2 2' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'square')

    @requirements(['#0012', '#0013'])
    def test_ask_valid_quadrilateral_question2(self):
        questions = Interface()
        inquiry = 'What type of quadrilateral is 2 3 2 3' + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'rectangle')

