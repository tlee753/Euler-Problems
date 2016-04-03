num1 = 1
num2 = 1
array = [num1, num2] # initialize the array
total = 0 # intitalize total

while (num2 < 4000000):
    array.append(num2)
    num2 += num1
    num1 = num2 - num1

for item in array:
    if (item % 2 == 0):
        total += item
print total
