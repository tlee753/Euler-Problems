"""
Euler Problem 1
===============
Sum all numbers less than 1000 that are divisible by 3 or 5

- created by tlee753
- last modified 4.21.16
"""

import time

startTime = time.time()
total  = 0 # initaialize total

for num in range(1, 1000): # iterate through natural numbers below 1000
    if (num % 3 == 0 or num % 5 == 0):
        total += num

print total
print " --- %s seconds --- " % (time.time() - startTime)
