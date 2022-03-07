# fname = 'romeo.txt'
fname = input("Enter file name: ")
fhand = open(fname)

words = list()
for line in fhand:
    line = line.strip()
    words_in_line = line.split()
    for word in words_in_line:
        if word in words : continue
        words.append(word)
words.sort()
print(words)
