numberOfPasses = 0
numberOfLosses = 0
for student in range(1,16):
    score = int(input(f"Enter the scores of student {student}:  "))
    if score < 45:
        numberOfLosses += 1
    else:
        numberOfPasses += 1

print(f"number of student that that pass {numberOfPasses} and number of student that failed {numberOfLosses}")
    
    
