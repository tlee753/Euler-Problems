"""
Euler Problem 6
===============

- created by tlee753
- last modified 4.21.16
"""

import time

startTime = time.time()
squaredTotal = 0
sumTotal = 0

for i in xrange(1, 101):
    sumTotal += i
    squaredTotal += i**2

print "The difference between sumed squares and square of sum is %d" % (sumTotal**2 - squaredTotal)
print " --- %s seconds --- " % (time.time() - startTime) 
