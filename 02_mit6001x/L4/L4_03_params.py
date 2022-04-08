def hello(first, last, is_reverse):
    if is_reverse == True:
        print(last, first, is_reverse)
    else:
        print(first, last, is_reverse)

hello('john', 'doe', False)
hello('doe', 'john', True)
hello('doe', 'john', is_reverse = True)
hello(is_reverse=False, first='john', last='doe')

# hello(first='john', last='doe', False) #breaks code
# hello(is_reverse=False, 'john', 'doe') # breaks code
# hello(is_reverse=False, first='john', 'doe') # breaks code


def hello_default(first = 'john', last='doe', is_reverse=False):
    if is_reverse == True:
        print(last, first, is_reverse)
    else:
        print(first, last, is_reverse)

hello_default()
hello_default('bob', is_reverse =False)
hello_default(last='smith', is_reverse =False)


# hello_default(False) # treats first argument as first params; no type detection
# hello_default('bob',, is_reverse =False) #breaks code
# hello_default('bob',last='smith', False) #breaks code
