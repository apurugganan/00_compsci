import re

fname = input('Enter file name: ')

if len(fname) < 1: fname = 'regex_sum_1447759.txt'

fhand = open(fname)

# get me a list of numbers
nums = list()
for line in fhand:
  temp = re.findall('[0-9]+',line)
  if len(temp) > 0:
    for item in temp:
      item = int(item)
      nums.append(item)

# add the numbers
total = 0
for num in nums:
  total += num

print(total)