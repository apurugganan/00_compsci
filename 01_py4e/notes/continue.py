n = input('Enter letter: ')

while n != 'a':
    n = input('Enter again 1st: ')
    if n == 'b':
        print('This is b')
        continue

    print('checkpoint 1')

    if n == 'c':
        print('This is c')
        break
    
    print('checkpoint 2')

    # n = input('Enter again 2nd: ')

print('END')