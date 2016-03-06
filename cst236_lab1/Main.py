"""
:mod:`source.Main`
============================================
Entrance module to testing programs
"""

import nose2

with open('QAFile.txt', 'w') as outFile:
    outFile.write("Questions and Answers")
    outFile.write('\n\n')
outFile.close()

nose2.discover()

