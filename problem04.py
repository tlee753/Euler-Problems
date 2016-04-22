"""
Euler Problem 4
===============

- created by tlee753
- last modified 4.5.16
"""

import time

ans = 0
startTime = time.time()

for i in xrange(999, 100, -1):
    for j in xrange(i, 100, -1):
        x = i * j
        string = str(x)
        if (string == string[::-1]):
            if (x > ans):
                ans = x

print ans
print "--- %s seconds --- " % (time.time() - startTime)
