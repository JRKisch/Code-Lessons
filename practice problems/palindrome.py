from englishWords import *

def isPalindrome(word):   
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

for word in englishWords():
    if isPalindrome(word):
        print(word)