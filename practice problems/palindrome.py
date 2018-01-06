from englishWords import *

def isPalindrome(word):
    # TODO Implement me!
    return word == "palindrome"

for word in englishWords():
    if isPalindrome(word):
        print(word)