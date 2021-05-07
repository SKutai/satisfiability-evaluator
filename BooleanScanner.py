'''
Satisfiability Evaluator
	@author William Clift
	@author Seraiah Kutai
	@date 5 May 2020

	Run:
		python boolean.py

'''

import re
from symbolTable import symbolTable

'''
Scanner class for boolean language
'''
class BooleanScanner:

    # data
    regexs = ['^[\s]+', '^(:=)', '^(\()', '^(0)', '^(1)', '^(AND)', '^(OR)', '^(NOT)', '^(XOR)', '^(\))', '^([a-zA-Z][a-zA-Z0-9]*)']
    types = ['spc', 'asgn', 'lpar', 'false', 'true', 'a', 'o', 'n', 'x', 'rpar', 'vari']
    lines = []
    pairs = []
    line_scanned = []

    def __init__(self, source):
        self.getInput(source)
        self.scanTokens()
        self.symbols = symbolTable()
        #self.scanInput()

    # read the input
    def getInput(self, s):
        #print('READING')
        with open(s) as f:
            self.lines = f.readlines()
            #print('read: ', self.lines)

    def scanTokens(self):
      for line in self.lines:
        linearr = []
        line = line.split(" ")
        for e in line:
          mat = None
          for regex in self.regexs:
              mat = re.match(regex, e)
              if mat is not None:
                self.pairs.append([self.types[self.regexs.index(regex)], mat.group()])
                linearr.append([self.types[self.regexs.index(regex)], e])
                break
        self.pairs.append(['spc', '\n'])
        self.line_scanned.append(linearr)
        #print(linearr)

    def resolveVar(self, name):
      result = self.symbols.getVal(name)
      if result == None:
        pass
      else:
        return result
'''
    def evaluateTerm(left, operation, right):
      if operation == 'AND':
        return left and right
      elif operation == 'OR':
        return left or right
      elif operation == 'NOT':
        return not left
      elif operation == 'XOR':
        if (left == True and right == False) or (left == False and right == True):
          return True
        else:
          return False

    def evaluate(line):
      value = None
      left_token = line[0]
      left_type = left_token[0]
      left_sym = left_token[1]

      if left_type == 'true' or left_type == 'false':
        operation == line[1]

      elif left_type == 'n':
        evaluate()

      elif left_type == 'lpar':
        subline = compileExpression(line)
        value = evaluate(subline, 0)
      elif left_type == 'vari':
        left_sym = resolveVar(left_sym)


      return value

    def parse(self):
      for line in self.line_scanned:
        value=evaluate(line)
'''
      

        

  

        
        


