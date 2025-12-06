numbers=[20,39,49,74,58,24,57,24,93,0,10]
sumOfevenPosition=0
for count in range(0, len(numbers)+1):
    if count%2==0:
        sumOfevenPosition+=numbers[count]
        print(count)
print(sumOfevenPosition)
