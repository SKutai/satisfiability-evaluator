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

    regexs = ['[a-zA-Z][a-zA-Z0-9]*', ':=', '(', '0', '1', 'AND', 'OR', 'NOT', 'XOR', ')']
    types = ['vari', 'asgn', 'lpar', 'false', 'true', 'a', 'o', 'n', 'x', 'rpar']
    lines = []
    pairs = []

    def __init__(self, source):
        self.getInput(source)

    def getInput(self, s):
        s = 'input.txt'
        with open(s) as f:
            self.lines = f.readlines()
            print('read: ', self.lines)

    def scanInput(self):
        for line in self.lines:
            words = line.split()
            for word in words:
                for regex in regexs:
                match = re.match(regex, word)
                if(match != None):
                  self.pairs.append([types[regexs.index(regex)], word])
