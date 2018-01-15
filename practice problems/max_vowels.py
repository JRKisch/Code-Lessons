from englishWords import *

def isVowel(character):
    return character in "aeiou"

def numberOfVowelsInAWord(word):
    maxNumberOfVowels = 0
    vowelsInRun = 0
    
    for i in range(len(word)):
        if isVowel(word[i]):
            vowelsInRun += 1
            maxNumberOfVowels = max(maxNumberOfVowels, vowelsInRun)
        else:
            vowelsInRun = 0
    
    return maxNumberOfVowels   
    
def findMaxVowels():
    maxSoFar = 0
    wordsWithMax = []
    for word in englishWords():
        numberVowels = numberOfVowelsInAWord(word)
        if numberVowels == maxSoFar:
            wordsWithMax += [word]
        elif numberVowels > maxSoFar:
            maxSoFar = numberVowels
            wordsWithMax = [word]
            
    print(wordsWithMax)

findMaxVowels()