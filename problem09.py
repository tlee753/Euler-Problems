"""
Euler Problem 9
===============

- created by tlee753
- last modified 4.22.16
"""

import time
from math import *

startTime = time.time()
found = False

for a in xrange(1, 1000):
    for b in xrange(a, 1000):
        c = 1000 - a - b
        if (c**2 == a**2 + b**2 and c > 0):
            found = True
            break
    if (found == True):
        ans = a*b*c
        break

print ans
print " --- %s seconds --- " % (time.time() - startTime)