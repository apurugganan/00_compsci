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
