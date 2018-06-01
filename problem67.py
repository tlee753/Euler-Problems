"""
Euler Problem 67
================

- created by tlee753
- last modified 6.1.18
"""

import time
import operator

startTime = time.time()

f = open("problem67.txt", "r")
pyramid = []

for l in f:
    l = l.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    pyramid.append(l)

f.close()

f = open("problem67.txt", "r")
maxPyramid = []

for l in f:
    l = l.split()
    for i in range(len(l)):
        l[i] = int(l[i])
    maxPyramid.append(l)

f.close()       

for h in range(1, len(pyramid)):
    for i in range(0, len(pyramid[h])):
        if i == 0:
            maxPyramid[h][i] += maxPyramid[h-1][0]
        elif i == len(pyramid[h])-1:
            maxPyramid[h][i] += maxPyramid[h-1][len(pyramid[h])-2]
        else:
            maxPyramid[h][i] += max(maxPyramid[h-1][i-1], maxPyramid[h-1][i])

i, v = max(enumerate(maxPyramid[h]), key=operator.itemgetter(1))

ans = v
    
print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))