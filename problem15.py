"""
Euler Problem 15
================

- created by tlee753
- last modified 5.31.18
"""

import time

startTime = time.time()

def fact(n):
    prod = 1
    while (n > 1):
        prod = prod * n
        n -= 1
    return prod

def pascalCenter(n):
    return int(fact(n*2) / (fact(n) * fact(n*2 - n)))

ans = pascalCenter(20)

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))