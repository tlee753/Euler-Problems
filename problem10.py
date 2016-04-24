"""
Euler Problem 10
================

- created by tlee753
- last modified 4.23.16
"""

import time
from math import *

startTime = time.time()
ans = 0

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
    
for i in range(0, 2000000):
    if isPrime(i):
        ans += i
        
print ans
print " --- %s seconds --- " % (time.time() - startTime)