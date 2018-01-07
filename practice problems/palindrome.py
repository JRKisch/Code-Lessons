from englishWords import *

def isPalindrome(word):
    c=-2
    R=word[-1]
    while c>=-len(word):
        R=R+word[c]
        c=c-1
    return word == R

for word in englishWords():
    if isPalindrome(word):
        print(word)
        
        