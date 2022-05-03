def apply_to_each(alist, afunc):
    for i in range(len(alist)):
        alist[i] = afunc(alist[i])

l = [1, -2, 3.4]

apply_to_each(l, abs) # => [1,2,3.4]
print(l)
apply_to_each(l, int) # => [1,2,3]
print(l)

def apply_funcs(alist_of_functions, x):
    for f in alist_of_functions:
        print(f(x))

apply_funcs([abs, int], 2)
# => 2
# => 2