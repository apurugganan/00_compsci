fname = input('Enter filename: ')
# fname = 'mbox-short.txt'

fhand = open(fname, 'r')

total = 0
count = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    line =  float(line[line.find(' '):])
    print(line)

    count = count + 1
    total = total + line

average = total / count

print('Average spam confidence:', average)
# print('Average spam confidence: %g' % average)
