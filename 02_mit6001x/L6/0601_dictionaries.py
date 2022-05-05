# my_obj = {key:value}
# my_obj['key'] # => returns value

my_obj = { 
    'name': 'bob', 
    1 : 8, 
    (2,4) : 'red', 
}

# Some Operations
print((2,4) in my_obj)

print(my_obj)
del(my_obj[1])
print(my_obj)

print(my_obj.keys())
print(my_obj.values())