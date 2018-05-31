"""
Euler Problem 13
================

- created by tlee753
- last modified 5.31.18
"""

import time

startTime = time.time()

f = open("problem13.txt", "r")

sum = 0

for l in f:
    sum += int(l)

ans = int(str(sum)[0:10])

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))