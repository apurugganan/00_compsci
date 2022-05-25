
# Multiplication Iterative Solution

def product(a,b):
    sum = 0
    while b > 0: 
        sum += a
        b -= 1 
    return sum

print(product(2,3))