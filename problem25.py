"""
Euler Problem 25 
================

- created by tlee753
- last modified 11/7/19
"""

import time

startTime = time.time()

fibNums = [0, 1, 1]
i = 1

while(True):
    i += 1
    
    while len(fibNums) < i+1:
        fibNums.append(0)
    
    fibNums[i] = fibNums[i-2] + fibNums[i-1]

    if len(str(fibNums[i])) >= 1000:
        ans = i
        break 

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))
