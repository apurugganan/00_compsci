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

## word counter
```  
lyrics = ['hello', 'world', 
    'beep', 'beep', 
    'foo', 'foo', 
    'python', 'python', 'python']

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict: 
            myDict[word] += 1
        else: 
            myDict[word] = 1
    return myDict

print('dict:', lyrics_to_frequencies(lyrics))


def most_common_words(freq): 
    values = freq.values()
    best = max(values)
    words = []
    for k in freq:
        if freq[k] == best:
            words.append(k)
    return (words, best) # return a tuple


common_words = lyrics_to_frequencies(lyrics)
print(common_words)
print('most:', most_common_words(common_words))


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(common_words, 2))
```

## Efficient Fibonacci
Inefficient fib
```
def fibonacci(num):
    if n == 1:
        return 1
    elif n == 2: 
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
```

Efficient fibonacci - memo-ization
keeping track of value already computed
```
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        answer = fib_efficient(n-1, d) + fib_efficient(n-2,d)
        d[n] = answer
        return answer

```

## Global Variables
- can be dangerous; 
- breakes scoping of variables by function call
```
# global keyword allows to change global variable
myvar = 1
def myfunc():
    global myvar
    myvar = 2
```

# Chapter 7
## Testing 
Testing 
Defensive Programming
Eliminate Source of Bugs - Debugging

Defensive Programming 
- write specifications (doc string)
- Modularize programs (break it up)
- check conditions on inputs/outputs (assertions)

Testing Validations
- compare inputs & outputs
- how to break the program

Debugging 
- study events leading up to an error
- why is not working
- how to fix the program

Set up
- design code to ease testing
- break it up to modules
- document constraints (what is input output)
- document assumptions

When are you ready to test
- ensure code runs (no syntax errors, no static semantic errors --things that dont form a well formed/written expression)

-set of expected results (input output)

Unit Testing 
- validate each piece of program
- test each function separately

Backend Retest
Regression Testing
- add test for bugs as you find them in a function
- catch reintroduced errors that previously were fixed 

Integration Testing 
- test the overall / emtire program

HOW
Test approaches
1. intuition - natural partition
2. if no natural partition, random testing
3. black box testing; explore paths through specification
4. glass box testing ; explore paths through code

Black Box Testing
- designed without looking the code
- can be reused
- build test cases in natural space partition

Glass Box Testing
- refers to the code directly for test design
- each branch; path-complete

## BUGS
- isolate 
- eradicate
- retest 

Overt vs covert
overt - obvious manifestation - code crashes / infinite loop
covert - no obvious / not behaving as expected

Persistent vs intermittent
- persistent everytime
- intermittent - occurs sometimes even if run on same input

Overt and Persistent
- obvious to detect

Overt and intermittent
- harder to debug; 
- conditions to reproduce;l can be handled

Covert
- dangerous; 
- not realize answers are incorrect until run for long period

## Debugging
print statements; what Im expecting, what I am seeing
systematic; test hypothesis
bisection method

think, draw, explain
backup code, change code


# Chapter 8 Exceptions and Assertions

## Exceptions
- procedure of execution hits an unexpected result/condition
ex. 
```
// IndexError: access an index beyond the limits
test = [1,2,3]
test[4]

// TypeError: trying to conver an inappropriate type
int(test) 

NameError: referencing a non-existing variable
a
```
SyntaxError     : Python cant parse program
NameError       : variable name not found
AttributeError  : attribute reference fails
TypeError       : operand doesnt have correct type
ValueError      : operand typoe okay but value is illegal
IOError         : IO system reports malfunction (file doesnt exist)

What to do
fail silently - bad idea; no warning; substitute value or continue
return an "error" value - complicates code; check special value; what value?
stop execution - raises an exception

### TRY-EXCEPT
```
try:
    Do something
except:
    Do something when try does not complete; exception is raised

# USING SPECIFIC ERRORS
try: 
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a/b)
    print(a+b)
except ValueError:
    print("Could not convert number")
except ZeroDivisionError:
    print("Cant divide by zero")
except: 
    print("Something went wrong")

# ELSE AND FINALLY
try: 
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a/b)
    print(a+b)
except ValueError:
    print("Could not convert number")
except ZeroDivisionError:
    print("Cant divide by zero")
except: 
    print("Something went wrong")
else: 
    # runs when try completes with no exceptions
finally:
    # always executed after try, else and except
    # even with a break, continue or return
    # will run no matter what else happened
```

## Raise
Exceptions as control flow
- dont return special values when error occured; my customized error message
- check whether 'error value' was returned
- decide when to raise an exception
- raise and exception when unable to produce a result consistent with function' specification 
```
# raise <exceptionName>(arguments)
raise ValueError("something is wrong")

def get_ratios(list1, list2):
    """
    Assumptions: list 1 nd 2 are lists of equal length
    Returns: a list containing list1[i] / list2[i]
    """
    ratio = []
    for index in range(len(list1)):
        try: 
            ratios.append(list2[index]/float(list2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('called function has bad arguments)
    return ratios

L1 = [1,2,3]
L2 = [4,5,6]
L3 = [7,8]
```

## Exception return a value 
```
def get_stats(class_list):
    new_stats = []
    for element in class_list:
        new_stats.append([element[0], element[1], average(element[1])])
    return new_stats

def average(grades):
    try: 
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        return 0.0 # return a value 

my_list = [
    "bob",[50,50,50],
    "john",[50,50,50],
    "charlie",[]
]
```

## Assertions
- raise and error if assumptions are not met
- dont allow programmer to control response to unexpected conditions
- ensure execution halts whenever expected condition is not met
- check inputs;can be used anywhere
- easier to locate a source of a bug
- both input and output

```
def avg(grades):
    assert not len (grades) == 0, 'no grades data'
    return sum(grades) / let(grades)
```

Where to use assertions
- supplement to testing
- raise exceptions to bad data input
- use assertions to 
    1. check types of values
    2. check invariants on data structs are met 
    3. check constraints on return values
    4. check violations of constraints on procedure (e.g no duplicates on a list)


## Objected Oriented Programming 
- data abstraction; 
- internal representation thru data attributes
- interface for interactong with an object is through methods
- defines behaviours but hides implementation
- can create new instance; destroy objects
- bundle data into packages; procedures work on them through well-defined interfaces

objects have: 
1. type 
2. data representation 
3. set of procedures for interaction with the object

each instance is a particular type of an object
123 is an instance of an int
a = "hello"; a is an instand of a string

NOTE: always use the defined interfaces; correct behavior may be compromised if you manipulate internal data representation

creating a class vs using instance of a class
creating
1. define the class name
2. define class attributes

using 
1. create new instances of objects
2. doing operations on the instance

## Class
```
class Name_of_Class(object):
    <define attributes>

# object means that the Name class is a python object and inherits all its attributes
# Name is a subclass of arg
# object is a superclass of Name
```

## Attributes
- data and procedures that "belong" to the class; 
- data attributes as other objects that make up the class
- procedural attributes(methods) as functions that work only with this class; ways to use data 

Define how to create an instance of a class
```
class Coordinate(object)
    def __init__(self, x,y):
        self.x = x
        self.y = y
```

instance.data
instance.method
c.x
- instance as a frame that we bound values to data
- c gets the value of c (a frame) and then look up the value associated with x
- "." used to access any attribute of the object

## Method
procedural attribute; function that only works with the class
SIDENOTE: python always passes the actual object as the first arugment; convention is to use self as the name of the argument
```
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    # self returns to an instance
    def distance(self, other): 
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

```

Calling methods
```
# conventional 
c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.distance(origin))
# object on which to call method
# inherits the distance from the class definition, automatically uses c as the first argument

# name of a class; 
print(Coordinate.distance(c, origin))

# using class to get to method  must provide both arguments
# get the value of Coordinate (a frame), looks up the value associated with distance(a procedure), then invokes it; requires two arguments
```

## String Representation | String Method
print representation of the instance; class object
```
print(c) # gives memory location; uninformative
         # within the main environment, this is the instance of the coordinate object and this is the memory location where it lies

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __str__(self):
        return "whatever you like" # needs to be a string

print(c)
```

## Type 
```
type(c)

# instance of a class and the class type is Coordinate
# __main__; defined up the enivornment of where I interact
```

## Special Operators
override built in special operators: +, -, =, < etc..
```
__add__
__sub__
__eq__ 
__lt__
__ln__
```

## Example
```
class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    # methods
    # getters and setters; preserve internal representation
    # separate internal and actual use representation
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    
    # override inherited methods
    def __add__(self, other):
        newNum = (self.getNum() * other.getDen()) + (other.getNum() * self.getDen())

        newDen = self.num() * other.num

        return fraction(newNum, newDen)
```