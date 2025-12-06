number = int(input("Enter a number from 1-10: "))
print("========== Multiplication Table =========" )
for multiple in range(1,11):
    result = number * multiple
#    print(f"{number} X {multiple} = {result}")
    
    print(number, "  * ", multiple, ' = ', result )
