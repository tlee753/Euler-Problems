"""
Euler Problem 12
================

- created by tlee753
- last modified 5.31.18
"""

import time

startTime = time.time()

i = 1
triangleNumber = 76576500

while (1):
    divisorCount = 0
    for j in range(1, int(triangleNumber/2) + 1):
        if (triangleNumber % j) == 0:
            divisorCount += 1
    
    if divisorCount > 500:
        ans = triangleNumber
        break

    i += 1
    triangleNumber += i

print (ans)
print (" --- %s seconds --- " % (time.time() - startTime))