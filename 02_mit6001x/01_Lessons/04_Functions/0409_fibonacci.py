# RECURSION: TWO BASE CASES
# two recursion calls to settle two base cases
# fibonacci sequence
def fib(x):
    """
    assumes x is an int >= 0
    returns Fibonacci of x
    """
    if x == 0 or x ==1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)