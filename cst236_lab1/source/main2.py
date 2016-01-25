from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.question_answers import get_fibonacci, get_some_pi, get_the_door, convert_unit_to_unit, simple_multiply

import difflib
import time
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}
        self.question_answers = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why"]
        self.question_mark = chr(0x3F)

        self.rebuild_question_answers_dictionary()

        self.commands = {
            'Please clear memory': QA('Please clear memory', self.rebuild_question_answers_dictionary),
            'Open the door hal': QA('Open the door hal', get_the_door)
        }

        self.last_question = None

    def rebuild_question_answers_dictionary(self):
        self.question_answers.clear()

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type),
            'What time is it': QA('What time is it', time.asctime()),
            'What is the n digit of fibonacci': QA('What is the n digit of fibonacci', get_fibonacci),
            'What is the n digit of pi': QA('What is the n digit of pi', get_some_pi),
            'Why did the chicken cross the road': QA('Why did the chicken cross the road', 'To prove to the '
                                                    'armadillo that it can be done'),
            'What is n multiplied by m': QA('What is n multiplied by m', simple_multiply),
            'What student really deserves an A': QA('What student really deserves an A', 'Kirt Stark does!')

        }

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            first_word = parsed_question[0:8].lower().__str__()
            if first_word == 'convert ':
                return self.send_for_conversion(question)
            for answer in self.commands.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except:
                            raise Exception("Too many extra parameters")
            else:
                return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except:
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    def send_for_conversion(self, question):
        words = []
        words = question.split(' ')

        if words.__len__() != 5:
            return "incorrect number of words in conversion question"

        try:
            num = float(words[1].strip(' '))
        except ValueError:
            return "error in number value"

        return convert_unit_to_unit(num, words[2].strip(' '), words[4].strip(' '))

