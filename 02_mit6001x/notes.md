# Intro to Computer Science and Programming in Python
by Eric Grimson

## Introduction to Python
variables; bindings
expressions
syntax
static semantic

branching program
if-elif-else statements
nested conditionals
compound boolean
linear programs - constant times


## Core Elements of Programs
### STRING
string - object; sequence of characters
```
great = hi + name; overloading strings
```
successive concatenation 
```
3*'hello
```
because data is nonscalar; indexing
```
'hello'[1]
```
String casting
```
str(1)
```


### INPUT-OUTPUT
Output: Print
```
print(x)
// comma ; prints sepearated by a space
print(x,1,"abc")
```

Input: input()
```
# enters as a string
text = input("Type something: ")
```

### CONTROL FLOW
1. Branching
2. Loops

### LOOPS
While Loop - use when unable to predict a condition
```
while <condition>:
    <code block>
    <condiition increment>
```
For Loop - use when a computation for the condition is used
```
for n in range(5)
    <expression>
```

Break: stops execution of loops
```
for n in range(5)
    <expression>
    if n == 3:
        break
```

## Chapter 2
Exhaustive Solutions
Guess and Check

## Chapter 3
Approximate Solutions
making guess using small increments

Bisection Search
pick in the middle, too big or too small, throw away half, repeat
ordering property, value increases monotolicly,

# Chapter 4
### Decomposition
able to break problems into different, self-contained, pieces

### Abstraction
supreess details of method to compute something rom use of that computation

### Function
reusable code; embodies Decompistion and Abstraction
Properties of a function
1. name
2. parameters
3. docstring
4. body
a new scope/frame/environment created when entering a function

```
any time i do an invocation of a function, i create a new frame, bind the formal parameter of the function to he values of the expressions past in and relative to that frame, i know evaluate the body of that expression, when Im done with the body of the expression, if there’s a return, I’m gonna send back the value of whoever called for it and erase and remove the frame cause I no longer need it
```

### Scope 
mapping of names to objects
can access variable defined outside but cannot modify variables defined outside

help: pythontutor.com

## Arguments
order matter unless if explicitly provided otherwise
able to provide a default value

## Specification
a contract between the implementer of a function and the user
- Assumptions; conditions must be met; typically constraints on values of paramater
- Guarantees: conditions the must be met by function, provided it has been called in manner consistent with assumptions  

## Docstring
```
def isEven(i): 
    """
    Input: i, a positive int
    Returns True if i is eve, otherwise False
    """
    return i % 2 == 0
```

## Recursion
programming technique where a function calls itself
must have 1 or more base case;
must solve the same problem on some oher input with goal of simplifying the larger problem input
divide and conquer algorithm


## Modules
importing code files to another
example:
```
import file
file.do_function()
```

Another way to import 
```
from file import *
do_function()

create bindings within current scope for all objects defined in file
statements within module are executed only the first time a module is imported
```

## Files
every os has its own way of handling files; Python provides an os independent means to access files, using a file handle
```
# creates a file named filename 
# returns a file handle which we can name and reference.
# argument 'w' that file can be write into
nameHandle = open('filename', 'w')
```
write to a file 
```
nameHandle.write('sometext' + '\') # '\' is a carriage return 
nameHandle.close()
```

# Chapter 5
## Tuples
ordered sequence of elements,
can be mixed
immutable, cannot change the element values
```
tuple = ()
tuple = (1, "2", 3)

tuple + (4,5)
print(tuple) # (1,"2",3,4,5)
tuple[0] # prints 1
```
comma in the tuple
```
t = (1,2,3)
t[1:2] # => (2,)
# comma in the tuple is identifier that it is infact a tuple
```

convenient way to switch values
```
(x,y) = (y,x)
```

return more than 1 value
```
def quotient_and_remainder(x,y):
    q = x // y
    r = x % y

    return (q,r)

(quot, rem) = quotient_and_remainder(4,5)
```

tuples are iterable
```
def get_data(a_tuple):
    nums = ()
    words = ()

    for t in a_tuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    
    return (min_nums, max_nums, unique_words)
```

## LIST 
order sequence of information, accessible by index
denoted by []
contains elements; maybe be mixed but not common
mutable
```
a_list = [1,2,'3', true]

# walk through a list
total = 0
for element in a_list:
    total += element

```
### List operators
```
a_list.append(4) # => [1,2,'3',true,4]

a_list.extend([5,6]) # => [1,2,'3',true,4,5,6]

del(a_list[3]) # => [1,2,'3',4]

a_list.pop() # => [1,2,'3']

a_list.remove('3') # => [1,2]; removes first instance of '3'

list('string') # => ['s','t','r','i','n','g']

'hello there'.split() # => ['hello', 'there']
'hello@there'.split() # => ['hello', 'there']

a_list = [a,b,c]
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
```

## RANGE
acts as a tuple
for el in range(1,2,3)


## ALIASING
List is an object in memory
```
hot = ['yellow','orange', 'red']
warm = hot

hot.append('pink') # will also change warm (points to the same object)
```

## CLONING
```
cool = ['blue, 'green', 'grey']
chill = cool[:]
```

## MUTATION 
avoid mutating a list as you are iterating over it
```
# unexpected outcome
def remove_duplicate(l1,l2):
    for el in l1:
        if eel in l2:
            l1.remove(el)

# correct way
def remove_duplicate(l1,l2):
    l1_copy = l1[:]
    for el in l1_copy:
        if eel in l2:
            l1.remove(el)

```


# OBJECT
Almost everything in python is an object; object have data, methods and functions

# FUNCTION AS OBJECTS
first class objects: type, can be elements of data structures can appear in expressions

passing function as arguments; high order programming
```
def apply_to_each(alist, afunc):
    for i in range(len(alist)):
        alist[i] = afunc(alist[i])

l = [1, -2, 3.4]

apply_to_each(l, abs) # => [1,2,3.4]
apply_to_each(l, int) # => [1,2,3]

def apply_funcs(alist_of_functions, x):
    for f in alist_of_functions:
        print(f(x))

apply_func([abs, int], 2)
# => 2
# => 2
```

## MAP
```
map(abs,[1, -2, 3, -4])
for el in map(abs, [1,-2,3,-4])
    print(el)

# general form - an n-ary function and n collections of arguments
l1 = [1,28,36]
l2 = [4,57,9]

for el in map(min,l1,l2):
    print(el)

[1,28,9]
```

## COMMON OPERATIONS: Strings, Tuples, Lists, Range
```
seq[i] # => get element of sequence
len(seq) # => length of sequence
seq1 + seq2 # => concatenation of sequence (not range) 
n * seq # => sequence that repeats seq n times (not range)
seq[start : end] # => slice of sequence
e in seq # => True if e is contained in seq
e in not in seq # seq => Tire if e is not in seq
for e in seq # => iterares over elememts of sequence
```

# CHAPTER 6
## DICTIONARIES
stores pairs of data: key and value; no order
mutable

keys must be unique; immutable; hashable; be wary of using float as key
values any type; can be a duplicate

```
my_obj = {key:value}

my_obj['key'] # => returns value

# Some Operations
'key' in my_obj
del(my_obj['key'])

my_obj.keys()
my_obj.values()
```

### Example

word counter
```  
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict: 
            myDict[word] += 1
        else: 
            myDict[word] = 1
    return myDict
```

