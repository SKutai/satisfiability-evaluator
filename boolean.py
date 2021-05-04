import re

class BooleanScanner:

    tokes = ['[a-zA-Z][a-zA-Z0-9]*', ':=', '(', '0', '1', 'AND', 'OR', 'NOT', 'XOR', ')']
    types = ['vari', 'asgn', 'lpar', 'false', 'true', 'a', 'o', 'n', 'x', 'rpar']
    lines = []

    def __init__(self, source):
        self.getInput(source)

    def getInput(self, s):
        s = 'input.txt'
        with open(s) as f:
            self.lines = f.readlines()
            print('read: ' + self.lines)

    def scanInput(self):
        for line in self.lines:
            words = line.split()
            for word in words:

