# Inefficient fib
def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2: 
        return 2
    else:
        return fibonacci(num-1) + fibonacci(num-2) 

# Efficient fibonacci - memo-ization
# keeping track of value already computed
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        answer = fib_efficient(n-1, d) + fib_efficient(n-2,d)
        d[n] = answer
        return answer

test = 40
d = { 1 : 1, 2 : 2}

print(fibonacci(test)) # run time will be a lot longer
print(fib_efficient(test, d))