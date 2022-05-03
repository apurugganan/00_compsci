map(abs,[1, -2, 3, -4])
for el in map(abs, [1,-2,3,-4]):
    print(el)

# general form - an n-ary function and n collections of arguments
l1 = [1,28,36]
l2 = [4,57,9]

for el in map(min,l1,l2):
    print(el)

# [1,28,9]