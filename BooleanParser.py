'''
terminals
val -> 0 | 1
op -> NOT | AND | OR | XOR

nonterminals
expr -> val op val | 
        val op expr |
        val
'''

# order of opperations: PRENTHESIS, NOT, AND, OR, XOR
# there is no print statement so the parser will always print the result after completing a command
class BooleanParser:

    tokens = []

    def __init__(self, tokens):
        self.tokens =  tokens
        parseTokens()

    def AND(a,b):
        if(a and b):
            return 1
        else:
            return 0

    def OR(a,b):
        if(a or b):
            return 1
        else:
            return 0

    def XOR(a,b):
        if(a and not b) or (b and not a):
            return 1
        else:
            return 0

    def NOT(a):
        if a:
            return 0
        else:
            return 1

    def parseTokens(self):
        count = 0
        for token in self.tokens:

            count += 1