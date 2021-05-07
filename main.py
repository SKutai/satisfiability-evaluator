import re
from BooleanScanner import *
from parse import *

scan = BooleanScanner('smallinput.txt')
tokenPairs = scan.pairs
#print(tokenPairs)

line_scanned = scan.line_scanned
print(line_scanned)
parse = Parse()

for e in line_scanned:
	parse.evaluate(e)

'''
for p in tokenPairs:
    print(p)
'''