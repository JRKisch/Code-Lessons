from englishWords import *

def isPalindrome(word):
    c=-1
    R=""
    while c>=-len(word):
        R=R+word[c]
        c=c-1
    return word == R

for word in englishWords():
    if isPalindrome(word):
        print(word)
        
        