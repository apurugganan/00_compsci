a_list = [1,2,'3', True]

# MUTATE A LIST

# ADD an element
a_list.append(4) # => [1,2,'3',true,4]

# ADD elements of a list
a_list.extend([5,6]) # => [1,2,'3',true,4,5,6]

# REMOVE using an index
del(a_list[3]) # => [1,2,'3',4]

# REMOVE from the end of the list
a_list.pop() # => [1,2,'3']

# REMOVE by finding first instance or argument
a_list.remove('3') # => [1,2]; removes first instance of '3'

# CREATE a list
list('string') # => ['s','t','r','i','n','g']

'hello there'.split() # => ['hello', 'there']
'hello@there'.split() # => ['hello', 'there']

a_list = ['a',"b",'c']
''.join(a_list) # => 'abc'
'_'.join(a_list) # => 'a_b_c'

# SORT a list
lst = [2,3,1]
lst.sort() # => [1,2,3]
lst.reverse() # => [3,2,1]

lst = [2,3,1]
sorted(lst) # => [1,2,3] creates a duplicate


# CONCATENATE
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2 # => [1,2,3,4,5,6]
