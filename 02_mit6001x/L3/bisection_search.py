# find square root of a given number

num = 144

min = 0.0
max = num

closest = 0.01
guesses = 0

#guess number: get the middle
guess = (max + min)/2.0

while abs(guess ** 2 - num) >= closest:
    guesses += 1
    print(guesses, guess, abs(guess ** 2 - num))

  #throw away half 
    if guess**2 < num:
        min = guess
    else:
        max = guess
  
  # middle of the new half
    guess = (min + max) / 2.0

print(guess, guess ** 2, abs(guess ** 2 - num))
print(num)