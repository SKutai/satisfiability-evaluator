import re
from BooleanScanner import *

scan = booleanScanner('input.txt')
scan.scanInput()
pairs = scan.pairs
print(pairs)