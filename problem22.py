"""
Euler Problem 22
================

- created by tlee753
- last modified 6.1.18
"""

import time
import csv

startTime = time.time()

with open("problem22.txt", "rb") as csvFile:
    reader = csv.reader(csvFile, delimiter=" ", quotechar="|")
    for row in reader:
        print(row)

print(5)
print(" --- %s seconds --- " % (time.time() - startTime))