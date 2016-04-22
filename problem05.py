"""
Euler Problem 5
===============

- created by tlee753
- last modified 4.6.16
"""

import time

startTime = time.time()
maxValue = (1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20) + 1
i = 0

while (i <= maxValue):
    i += 20
    if ( i%11 == 0 and i%12 == 0 and i%13 == 0 and i%14 == 0 and i%15 == 0 and i%16 == 0 and i%17 == 0 and i%18 == 0 and i%19 == 0 and i%20 == 0):
        ans = i
        break

print ans
print " --- %s seconds --- " % (time.time() - startTime)

