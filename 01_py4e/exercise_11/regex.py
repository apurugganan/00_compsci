# REGEX

import re

fname = input('Enter file name: ')
if len(fname) < 1: fname = "mbox-short.txt"

str = 'dog cat bird'

y = re.search(' b*', str)
z = re.search(' b+', str)
print(y)
print(z)
