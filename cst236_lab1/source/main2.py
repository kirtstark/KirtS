from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.question_answers import get_fibonacci, get_some_pi, get_the_door, convert_unit_to_unit, simple_multiply,\
    cube_of_number, divide_evenly, paycheck, density_check, struggle_reason
from git_utils import is_file_in_repo, get_git_file_info, get_file_info, get_repo_branch, get_repo_url, get_repo_root

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
        self.file_name = ''
        self.result_out = open('QAFile.txt', 'a')

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Is"]
        self.question_mark = chr(0x3F)

        self.rebuild_question_answers_dictionary()

        self.commands = {
            'Please clear memory': QA('Please clear memory', self.rebuild_question_answers_dictionary),
            'Open the door hal': QA('Open the door hal', get_the_door),
            'Hal, take the garbage out.': QA('Hal, take the garbage out.', 'I am busy right now, you do it.')
        }

        self.last_question = None

    def __del__(self):
        self.result_out.close()

    def closing(self):
        self.result_out.close()

    def opening(self):
        self.result_out = open('QAFile.txt', 'a')

    def rebuild_question_answers_dictionary(self):
        self.question_answers.clear()

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quadrilateral_type),
            'What time is it': QA('What time is it', time.asctime()),
            'What is the n digit of fibonacci': QA('What is the n digit of fibonacci', get_fibonacci),
            'What is the digit of pi': QA('What is the digit of pi', get_some_pi),
            'Why did the chicken cross the road': QA('Why did the chicken cross the road', 'To prove to the '
                                                    'armadillo that it can be done'),
            'What is n multiplied by m': QA('What is n multiplied by m', simple_multiply),
            'What student really deserves an A': QA('What student really deserves an A', 'Kirt Stark does!'),
            'What is the cube of ': QA('What is the cube of ', cube_of_number),
            'How many times will divide completely into ': QA('How many times will divide completely into ',
                                                            divide_evenly),
            'What is when it is multiplied by and then added to ': QA('What is when it is'
                                                    ' multiplied by and then added to ', paycheck),
            'What is the mass of a measure of with a volume of cubic meters?': QA('What is the mass of a measure of'
                                                    ' with a volume of cubic meters?', self.send_for_density),
            'Why are these labs such a struggle for me': QA('Why are these labs such a struggle for me',
                                                            struggle_reason),
            'Is the <file name> in the repo': QA('Is the in the repo', is_file_in_repo),
            'What is the status of <file name>': QA('What is the status of ', get_git_file_info),
            'What is the deal with <file name>': QA ('What is the deal with ', get_file_info),
            'What branch is <file path>': QA('What branch is ', get_repo_branch),
            'Where did <file path> come from': QA('Where did come from', get_repo_url),
            'What is the repo root for <file path>': QA('What is the repo root for ', get_repo_root)
        }
        return "done"

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        self.result_out.write(question)
        self.result_out.write('\n')
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
                theAnswer = self.send_for_conversion(question)
                self.result_out.write(str(theAnswer))
                self.result_out.write('\n\n')
                return theAnswer
            for answer in self.commands.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        self.result_out.write(str(answer.value))
                        self.result_out.write('\n\n')
                        return answer.value
                    else:
                        try:
                            theAnswer = answer.function(*args)
                            self.result_out.write(str(theAnswer))
                            self.result_out.write('\n\n')
                            return theAnswer
                        except:
                            self.result_out.write("I have no response for that")
                            self.result_out.write('\n\n')
                            raise Exception("Too many extra parameters")
            else:
                self.result_out.write(NOT_A_QUESTION_RETURN)
                self.result_out.write('\n\n')
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
            self.file_name = ''
            split_parsed_question = parsed_question.split(' ')
            for wordy in split_parsed_question:
                file_word_list = wordy.strip('.')
                file_word_list = file_word_list.split('.')
                if file_word_list.__len__() > 1:
                    args.append(wordy)
                    split_parsed_question.remove(wordy)
                    parsed_question = ''
                    for each_word in split_parsed_question:
                        parsed_question += "{0} ".format(each_word)
                    parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        self.result_out.write(str(answer.value))
                        self.result_out.write('\n\n')
                        return answer.value
                    else:
                        try:
                            theAnswer = answer.function(*args)
                            self.result_out.write(str(theAnswer))
                            self.result_out.write('\n\n')
                            return theAnswer
                        except:
                            self.result_out.write("I have no response for that")
                            self.result_out.write('\n\n')
                            raise Exception("Too many extra parameters")
            else:
                self.result_out.write(UNKNOWN_QUESTION)
                self.result_out.write('\n\n')
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

    def send_for_density(self, vol=0):
        words = []
        words = self.last_question.split(' ')

        return density_check(words[8], vol)

