a_list = [1,2,'3', True]

a_list.append(4) # => [1,2,'3',true,4]

a_list.extend([5,6]) # => [1,2,'3',true,4,5,6]

del(a_list[3]) # => [1,2,'3',4]

a_list.pop() # => [1,2,'3']

a_list.remove('3') # => [1,2]; removes first instance of '3'

list('string') # => ['s','t','r','i','n','g']

'hello there'.split() # => ['hello', 'there']
'hello@there'.split() # => ['hello', 'there']

a_list = ['a',"b",'c']
''.join(a_list) # => 'abc'
'_'.join(a_list) # => 'a_b_c'

