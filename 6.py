wordlist = []
fname = input('Enter file:')
fhand = open(fname)
for line in fhand:
    h = line.rstrip()
    words = h.split()
    for word in words:
        if word in wordlist: continue
        wordlist.append(word)
wordlist.sort()
print(wordlist)
