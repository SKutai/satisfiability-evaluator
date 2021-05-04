'''
Satisfiability Evaluator
	@author William Clift
	@author Seraiah Kutai
	@date 5 May 2020

	Run:
		python boolean.py

'''

import re

'''
Scanner class for boolean language
'''
class BooleanScanner:

    # data
    regexs = ['^[\s]+', '^(:=)', '^(\()', '^(0)', '^(1)', '^(AND)', '^(OR)', '^(NOT)', '^(XOR)', '^(\))', '^([a-zA-Z][a-zA-Z0-9]*)']
    types = ['spc', 'asgn', 'lpar', 'false', 'true', 'a', 'o', 'n', 'x', 'rpar', 'vari']
    lines = []
    pairs = []

    def __init__(self, source):
        self.getInput(source)
        self.scanInput()

    # read the input
    def getInput(self, s):
        print('READING')
        with open(s) as f:
            self.lines = f.readlines()
            print('read: ', self.lines)

    # translate the input into an array of pairs as in [type, token]
    def scanInput(self):
        print('SCANNING')
        mat = None
        for line in self.lines:
            print('NEW LINE')
            while len(line) > 0:
                print(line)
                matched = False
                for regex in self.regexs:
                    if(not matched):
                        mat = re.match(regex, line)
                        if(mat is not None):
                            self.pairs.append([self.types[self.regexs.index(regex)], mat.group()])
                            line = line[mat.span()[1]:]
                            matched = True