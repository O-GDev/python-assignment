numbers=[20,39,49,74,58,24,57,24,93,0,10]
sumOfList=0
count=0
for count in range(0, len(numbers)):
    sumOfList+=numbers[count]
    count+=1

average = sumOfList/count
print(average)
