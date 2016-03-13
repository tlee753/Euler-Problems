import math

count = 0
# initialize letter counter

onesArray = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# letter count for one through nineteen
tensArray = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
# zero, ten, twenty, thirty

for i in range(1,102):
# iterates through all number from 'one' to 'one thousand'
    string = str(i)
    # converts the number into a string

    if len(string) == 1:
        count += onesArray[i]
    
    if len(string) == 2:

        if i < 20:
            count += onesArray[i]
        else:
            firstDigit = int(string[0])
            secondDigit = int(string[1])
            count += tensArray[firstDigit]
            count += onesArray[secondDigit]

    if len(string) == 3:
        firstDigit = int(string[0])
        secondDigit = int(string[1])
        thirdDigit = int(string[2])

        count += onesArray[firstDigit]
        # adds ones digit that starts a three digit number
        
        if i % 100 == 0:
            count -= 3
        # special case where 'and' isn't included

        count += 10
        # hard code for 'hundred' and 'and'

        if int(string[1:2]) < 20:
            count += onesArray[int(string[1:2])]
        else:
            count += tensArray(secondDigit)
            count += onesArray(thirdDigit)

    if len(string) == 4:
        count += 11
        # hard code for 'one thousand'

print count
