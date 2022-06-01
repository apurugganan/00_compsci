try: 
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(a/b)
    print(a+b)
except ValueError:
    print("Could not convert number")
except ZeroDivisionError:
    print("Cant divide by zero")
except: 
    print("Something went wrong")
else: 
    # runs when try completes with no exceptions
    print("everything ok")
    
finally:
    print("print no matter what happens")
    # always executed after try, else and except
    # even with a break, continue or return
    # will run no matter what else happened