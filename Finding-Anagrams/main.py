# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    str1 = input("Please input word: ")
    str2 = input("Please input anagram: ")

    str1 = str1.lower()
    str2 = str2.lower()
    if(len(str1) == len(str2)):

     sorted_str1 = sorted(str1)
     sorted_str2 = sorted(str2)

    if(sorted_str1== sorted_str2):
        return True
    else:
        return False
    #return True

print(find_anagram(str, str))