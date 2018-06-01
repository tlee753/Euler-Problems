"""
Euler Problem 21
================

- created by tlee753
- last modified 6.1.18
"""

import time

startTime = time.time()

import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)

def sumDivisors(n):
    if n == 0:
        return 0
    aList = list(divisorGenerator(n))
    aList.pop()
    return sum(aList)

myList = []
for i in range(1,10000):
    value = sumDivisors(i)
    if sumDivisors(value) == i and i != value:
        myList.append(i)

ans = sum(myList)

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))