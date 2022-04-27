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




```




Almost everything in python is an object; object have data, methods and functions