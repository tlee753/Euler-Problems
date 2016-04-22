"""
Euler Problem 17
================
Iterates through every number from one to one thousand, counting the number of letters

- created by tlee753
- last modified 3.13.16
"""

import math
import time

startTime = time.time()
# initialize timer

count = 0
# initialize letter counter

onesArray = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# letter count for one through nineteen
tensArray = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
# zero, ten, twenty, thirty

for i in range(1,1001):
# iterates through all number from 'one' to 'one thousand'

    string = str(i)
    # converts the number into a string

    if len(string) == 1:
    # one digit numbers
        count += onesArray[i]
    
    if len(string) == 2:
    # two digit numbers

        if i < 20:
            count += onesArray[i]
        else:
            count += tensArray[int(string[0])]
            count += onesArray[int(string[1])]

    if len(string) == 3:
    # three digit numbers
       
        count += onesArray[int(string[0])]
        # adds ones digit that starts a three digit number
        
        if i % 100 == 0:
            count -= 3
        # special case where 'and' isn't included

        count += 10
        # hard code for 'hundred' and 'and'

        if int(string[1:3]) < 20:
            count += onesArray[int(string[1:3])]
        else:
            count += tensArray[int(string[1])]
            count += onesArray[int(string[2])]

    if len(string) == 4:
    # four digit numbers

        count += 11
        # hard code for 'one thousand'

print count
print " --- %s seconds --- " % (time.time() - startTime)
