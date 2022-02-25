# PYTHON 4 Everyone

string.find() : returns position of first instance of the argument or -1 if there is none
```
x = 'a b c'
position = x.find(b)
print(position)
# prints => 2
```

re.search('searchterm', string) : returns Match object if exists or None if it doesnt exist
```
x = 'a b c'
match = re.seacrh('b', x)
print(match)
# prints => <re.Match object; span=(2, 3), match='b'>
```

abc*        matches a string that has ab followed by zero or more c
abc+        matches a string that has ab followed by one or more c
abc?        matches a string that has ab followed by zero or one c

```
str = 'dog cat bird'

y = re.search(' b*', str)
z = re.search(' b+', str)
print(y) # prints => <re.Match object; span=(3, 4), match=' '>
print(z) # prints => <re.Match object; span=(7, 9), match=' b'>
```

## Error
You probably named your file socket.py, if you did so, change it and try again.
```
>>> import socket
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\AJP\Desktop\ossu\01_py4e\socket.py", line 19, in <module>
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
AttributeError: partially initialized module 'socket' has no attribute 'AF_INET' (most likely due to a circular import)
>>>
```