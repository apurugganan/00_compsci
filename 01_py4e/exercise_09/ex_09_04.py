fname = input('Enter file: ')
if len(fname) < 1: fname = 'mbox-short.txt'

fhandle = open(fname)

# build a dictionary counting number of times sender sent a message
sender = {}
for line in fhandle:
  # ignore lines that doesnt start with 'From'
  if not line.startswith('From '): 
    continue
  line = line.rstrip()
  words = line.split()
  
  sender[words[1]] = sender.get(words[1], 0) + 1

bigname = None
bigvalue = None

for key,value in sender.items():
  if bigname is None or value > bigvalue:
    bigname = key
    bigvalue = value

print(bigname, bigvalue)

for key in sender:
  print(key)










