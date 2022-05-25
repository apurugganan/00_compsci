# scope 
#  Example 1
def func_1(x):
    x = 2
    print(x)

x = 1
func_1(x)
print(x)

# Example 2
def func_2(a):
    print(b) # goes up to look at outside

b = 1
func_2(b)
print(b)

# Example 3
o = 1
def func_3(n):
    o = o + 1
    print(o)

func_3(o)
print(o)