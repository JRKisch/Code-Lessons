def englishWords():
    f = open('dictionary.txt', 'r')
    for word in f:
        if len(word) > 0:
           yield word.strip()
