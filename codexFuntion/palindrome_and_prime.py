def check_palindrome(number):
    new_number = number
    reversed_number = 0
    while(new_number != 0):
        reversed_number+=(new_number%10)
        reversed_number*=10
        new_number//=10
    reversed_number//=10
    print(reversed_number)
    if(number == reversed_number):
        return True
    return False

def check_prime(number):
    factor_count = 0
    for count in range(1, number+1):
            if(number%count == 0):
                factor_count+=1
                print(count)
    if factor_count == 2:
        print("True")
        return True
    print("False")
    return False

def check_for_palindrome_and_prime(number):
    if check_prime(number) and check_palindrome(number):
        print('True')
        return True
    print("False")
    return False

check_for_palindrome_and_prime(10)
