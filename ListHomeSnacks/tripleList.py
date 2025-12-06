def tripleList(numbers):
    newNumbers=[]
    cube = 1
    for count in range(len(numbers)):
        for _ in range(3):
            cube*=numbers[count]
            newNumbers.append(cube)
        cube=1
    return newNumbers

print(tripleList([2,3,4]))



def evenAndOdd(numbers):
    boolean_value = []
    for count in range(len(numbers)):
        if numbers[count]%2==0:
            boolean_value.append("False")
        else:
            boolean_value.append("True")
    return boolean_value

print(evenAndOdd([1,2,3]))
