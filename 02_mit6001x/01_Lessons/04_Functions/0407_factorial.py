
# Recursion: Factorial n! = n * (n-1) * (n-2) ... * 1
def factorial(n):
    if n == 1: 
        return 1
    else:
        return n * factorial(n-1)
    
