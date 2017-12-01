"""
Euler Problem 12
================

- created by tlee753
- last modified 12.1.17
"""

import time

startTime = time.time()

solved = False
myList = [0, 1]
i = 2

while (not solved):
    myList.append(i + myList[i - 1])
    value = myList[i]

    primeFactorizationCount = []
    for j in range(2, value):
        if (value % j == 0):
            value /= j
            count = 2
            while (value % j == 0):
                value /= j
                count += 1
            primeFactorizationCount.append(count)

    product = 1
    for j in range(len(primeFactorizationCount)):
        product *= primeFactorizationCount[j]

    if product >= 500:
        solved = True
        ans = myList[i]
    
    i += 1

print ans
print " --- %s seconds --- " % (time.time() - startTime)