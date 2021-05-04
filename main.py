import re
from BooleanScanner import *

scan = BooleanScanner('input.txt')
scan.scanInput()
pairs = scan.pairs
print(pairs)