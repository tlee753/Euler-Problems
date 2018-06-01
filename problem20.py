"""
Euler Problem 20
================

- created by tlee753
- last modified 6.1.18
"""

import time

startTime = time.time()

def fact(n):
    prod = 1
    while n > 1:
        prod *= n
        n -= 1
    return prod

value = str(fact(100))

sum = 0
for c in value:
    sum += int(c)

ans = sum

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))