"""
Euler Problem 18
================

- created by tlee753
- last modified 5.31.18
"""

import time

startTime = time.time()

pyramid = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

maxPyramid = pyramid

for h in range(1, len(pyramid)):
    print("h is " + str(h))
    for i in range(0, len(pyramid[h])):
        if i == 0:
            maxPyramid[h][i] += maxPyramid[h-1][0]
        elif i == len(pyramid[h])-1:
            maxPyramid[h][i] += maxPyramid[h-1][len(pyramid[h])-2]
        else:
            maxPyramid[h][i] += max(maxPyramid[h-1][i-1], maxPyramid[h-1][i])



# dynamic programming, add values together running down the list based on max of parents (or parent for edge cases)
# once you've created a max pyramid, find the max at the bottom, work your way upward based on the maxes, gathering indexes as you go
# using indexes to generate path to answer

# h = 0
# i = 0
# path = []
# path.append(pyramid[h][i])

# while(h < len(pyramid) - 1):
#     h += 1

#     if (pyramid[h][i] > pyramid[h][i+1]):
#         path.append(pyramid[h][i])
#     else:
#         path.append(pyramid[h][i+1])
#         i += 1

#     print(path)
    
#     for j in pyramid[h]:
#         if (sum(path[0:h-abs(i-j)]) + j) > sum(path):
#             print("hello world")
#             # insert recursive a-star algo


ans = maxPyramid
    
print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))