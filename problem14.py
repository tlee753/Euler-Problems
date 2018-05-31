"""
Euler Problem 14
================

- created by tlee753
- last modified 5.31.18
"""

import time

startTime = time.time()

i = 1
chainLengthMax = 0

while (i < 1000000):
    chainLength = 1

    j = i
    while (j != 1):
        if (j % 2 == 0):
            j = j / 2
        else:
            j = 3*j + 1
        chainLength += 1
    
    if chainLength > chainLengthMax:
        ans = i
        chainLengthMax = chainLength

    i += 1

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))