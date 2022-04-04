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