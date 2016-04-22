"""
Euler Problem 7
===============

- created by tlee753
- last modified 4.21.16
"""

import time
from math import *

startTime = time.time()
count = 1
primeCount = 1

def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number)) + 1):
        if number % i == 0:
           return False
    return True

while (True):
    count += 2
    if (isPrime(count)):
        primeCount += 1
        if (primeCount == 10001):
            ans = count
            break    

print ans
print " --- %s seconds --- " % (time.time() - startTime)
