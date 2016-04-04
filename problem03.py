"""
Euler Problem 3
===============
Find the greatest factor for a given number

- created by tlee753
- last modified 4.4.16
"""

n = 50 # initialize the number in question
i = 3 # initialize the smallest integer factor greater than 2

while (n % 2 == 0): # remove all factors of two
    n = n / 2

while (n != 1):
    while (n % i == 0):
        ans = i
        n = n / i
    i += 2


print 'The greatest prime factor is ', ans
