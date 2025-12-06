def lenghtOfString(word):
    total_count=0
    for _ in str(word):
        total_count+=1
    print(total_count)
    return total_count


def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    print(reversed_word)
    return reversed_word

def time(minutes):
    hour = minutes/60
    seconds = minutes*60
    print(f"minutes in sec is {seconds} and in hour is {hour}")
    return f"minutes in sec is {seconds} and in hour is {hour}"
    
#lenghtOfString("gbogo")

def check_vowel(word):
        vowel_count = 0
        vowel_counted = ""
        not_repeated_vowel = ""
        counter = 0
        for letter in word:
            if letter in ("a","e","i","o","u"):
                if letter not in vowel_counted:
                    vowel_counted += letter
                    print("Vowels counted = ", vowel_counted)
                    vowel_count +=1
        print(vowel_count)
        print("Counter = ", counter)
        print("vOWEL COUNT = ", vowel_count)
        
        return vowel_count
                
#check_vowel("Pineapple")
