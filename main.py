import re
from BooleanScanner import *

scan = BooleanScanner('input.txt')
tokenPairs = scan.pairs
print("Pairs")
for p in tokenPairs:
    print(p)