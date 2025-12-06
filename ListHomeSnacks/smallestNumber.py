numbers=[20,39,49,74,58,24,57,24,93,0,10]
sumOfList=0
counter=0
smallestNumber=0
for count in range(0, len(numbers)):
    if numbers[count] < smallestNumber:
        smallestNumber = numbers[count]


print(smallestNumber)
