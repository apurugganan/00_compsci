fname = input('Enter file: ')

if len(fname) < 1: fname = "mbox-short.txt"

fhand = open(fname)

hour = {}
for line in fhand:
  if not line.startswith('From '):
    continue
  line = line.strip()
  words = line.split()
  words[5] = words[5].split(":")[0]

  hour[words[5]] = hour.get(words[5], 0) + 1

l = list()
for key, value in list(hour.items()):
  l.append((key, value))

l.sort()

for key,value in l:
  print(key, value) 