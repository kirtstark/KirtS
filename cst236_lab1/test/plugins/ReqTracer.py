"""
:mod:`ReqTracer`
============================================
Used by tests to connect tests with requirements
"""

from nose2.events import Plugin


class RequirementTrace(object):
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []


class JobStoryTrace(object):
    js_text = ""

    def __init__(self, text):
        self.js_text = text
        self.js_trace = []

Requirements = {}
StoryRequirements = []


def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


def story(story_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for this_story in story_list:
                in_there = 0
                for trace_story in StoryRequirements:
                    if this_story.lower() == trace_story.js_text.lower():
                        in_there = 1
                        trace_story.js_trace.append(func.__name__)
                if in_there < 1:
                    raise Exception('Story \"{0}\" not defined'.format(this_story))
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


with open('ProjectRequirement.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)
        elif 'for example' in line:
            intro, story_text, desc = line.split('\"', 2)
            StoryRequirements.append(JobStoryTrace(story_text))


class PrintOut(Plugin):
    configSection = 'Req-tracer'

    def afterSummaryReport(self, event):
        with open('outputFile.txt', 'w') as outFile:
            for req in Requirements:
                outFile.write(req)
                outFile.write(': ')
                outFile.write(Requirements[req].req_text)
                for functionName in Requirements[req].func_name:
                    outFile.write('\n\t\t')
                    outFile.write(functionName)
                outFile.write('\n\n')
            for question in StoryRequirements:
                outFile.write(question.js_text)
                outFile.write(': ')
                for functionName in question.js_trace:
                    outFile.write('\n\t\t')
                    outFile.write(functionName)
                outFile.write('\n\n')
        outFile.close()
