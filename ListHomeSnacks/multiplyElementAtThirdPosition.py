numbers=[20,39,49,74,58,24,57,24,93,0,10]
multiply=1
for count in range(2,len(numbers),3):
    multiply *= numbers[count]
    print(numbers[count])
print(multiply)


