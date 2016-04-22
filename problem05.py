"""
Euler Problem 5
===============

- created by tlee753
- last modified 4.6.16
"""

import time
import math

startTime = time.time()
maxValue = (math.factorial(20))
i = 11*20

while (i <= maxValue):
    i += 20
    if (i%11 == 0 and i%12 == 0 and i%13 == 0 and i%14 == 0 and i%15 == 0 and i%16 == 0 and i%17 == 0 and i%18 == 0 and i%19 == 0):
        ans = i
        break

print ans
print " --- %s seconds --- " % (time.time() - startTime)

