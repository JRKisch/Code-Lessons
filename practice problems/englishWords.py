def englishWords():
    f = open('dictionary.txt', 'r')
    for word in f:
        word = word.strip()
        if len(word) > 0:
           yield word
