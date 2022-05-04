
# seq[i] # => get element of sequence
# len(seq) # => length of sequence
# seq1 + seq2 # => concatenation of sequence (not range) 
# n * seq # => sequence that repeats seq n times (not range)
# seq[start : end] # => slice of sequence
# e in seq # => True if e is contained in seq
# e in not in seq # seq => True if e is not in seq
# for e in seq # => iterares over elememts of sequence
seq = "hello "
seq2 = 'there'

print(seq[1])
print(len(seq))
print(seq + seq2)
print(3 * seq)
print(seq[0:1])
print('h' in seq)
print('z' not in seq)
for e in seq:
    print(e)


seq = ['a','b', 'c']
seq2 = ['x', 'y', 'z']


print(seq[1])
print(len(seq))
print(seq + seq2)
print(3 * seq)
print(seq[0:1])
print('b' in seq)
print('d' not in seq)
for e in seq:
    print(e)