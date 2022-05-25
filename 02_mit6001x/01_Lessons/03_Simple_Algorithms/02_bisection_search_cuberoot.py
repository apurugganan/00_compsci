# given a number find cuberoot

num = 27
min = 0
max = num

diff = 0.001

guess = (max + min) / 2
counter = 1

while abs(guess**3 - num) >= diff: 
    print('guess no. = {} | guess {} | closeness {}'.format(counter, guess, diff))
    counter += 1

    if guess**3 < num: 
        min = guess
    else:
        max = guess

    guess = (max + min) / 2

print('end with closest num is', guess)