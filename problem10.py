"""
Euler Problem 10
================

- created by tlee753
- last modified 4.23.16
"""

import time

startTime = time.time()
sieve = [True] * 2000000

def multiplesCheck (sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: multiplesCheck(sieve, x)

ans = sum(i for i in xrange(2, len(sieve)) if sieve[i])

print ans
print " --- %s seconds --- " % (time.time() - startTime)