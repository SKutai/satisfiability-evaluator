'''
Satisfiability Evaluator
	@author William Clift
	@author Seraiah Kutai
	@date 5 May 2020

	Run:
		python boolean.py

'''

import re

class BooleanScanner:

    # data
    regexs = ['[a-zA-Z][a-zA-Z0-9]*', ':=', '(', '0', '1', 'AND', 'OR', 'NOT', 'XOR', ')']
    types = ['vari', 'asgn', 'lpar', 'false', 'true', 'a', 'o', 'n', 'x', 'rpar']
    lines = []
    pairs = []

    def __init__(self, source):
        self.getInput(source)

    # read the input
    def getInput(self, s):
        s = 'input.txt'
        with open(s) as f:
            self.lines = f.readlines()
            print('read: ', self.lines)

    # translate the input into an array of pairs as in [type, token]
    def scanInput(self):
        mat = None
        for line in self.lines:
            words = line.split()
            for word in words:
                matched = False
                for regex in self.regexs:
                    mat = re.match(regex, word)
                    if(not matched and mat is not None): # readability 100
                        self.pairs.append([self.types[self.regexs.index(regex)], word])
                        matched == True

        print('pairs: ', self.pairs)
