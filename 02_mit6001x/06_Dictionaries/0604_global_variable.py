myvar = 1
def myfunc():
    global myvar
    myvar = 2 #changes global var; not limited in scope

myfunc()
print(myvar)