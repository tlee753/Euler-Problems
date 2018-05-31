"""
Euler Problem 16
================

- created by tlee753
- last modified 5.31.18
"""

import time
import math

startTime = time.time()

value = str(int(math.pow(2, 1000)))

sum = 0
for c in value:
    sum += int(c)

ans = sum

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))