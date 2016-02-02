import random


class QA(object):
    def __init__(self, question, answer):
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer

class Reason(object):
    def __init__(self):
        self.reasons = ['I do not know.', 'Maybe it is the frequent napping.', 'Have you considered studying?',
               'It is supposed to be difficult, that is how you learn', 'Um, how much have you had to drink?',
               'Your lack of Python knowledge plays into it . . .', 'Too much goofing off', 'Alien abduction.',
               'Brain damage. Definitely brain damage.']

    def get_reason(self):
        random.seed()
        selection = random.randint(0, self.reasons.__len__() - 1)
        return self.reasons[selection]