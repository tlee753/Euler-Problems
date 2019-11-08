"""
Euler Problem 23 
================

- created by tlee753
- last modified 11/7/19
"""

import time

startTime = time.time()

with open('problem22-names.txt', 'r') as file:
    data = file.read().replace('"', '')

names = data.split(",")
names.sort()

ans = 0
for i in range(len(names)):
    nameSum = 0
    for l in names[i]:
        nameSum += ord(l) - 64
    ans += nameSum * (i+1)

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))
