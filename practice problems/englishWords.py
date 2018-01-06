def englishWords():
    f = open('dictionary.txt', 'r')
    for word in f:
        yield word.strip()
