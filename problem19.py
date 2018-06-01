"""
Euler Problem 19
================

- created by tlee753
- last modified 6.1.18
"""

import time
import datetime

startTime = time.time()

sundays=0
for year in range(1901,2001):
	for month in range(1,13):
		if datetime.date(year, month, 1).weekday() == 6:
			sundays+=1

ans = sundays

print(ans)
print(" --- %s seconds --- " % (time.time() - startTime))
from datetime import date