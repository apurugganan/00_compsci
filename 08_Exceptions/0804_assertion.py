def enter_2(num, txt):
    assert type(num) == int, 'not an integer'
    assert type(txt)  == str, 'not a string'

    sum = num + 2
    assert sum == 4, 'num is not 2'

    return sum

print(enter_2(2, 'hello'))


# breaks code; asserts values
print(enter_2(1.8, 'hello'))
print(enter_2(2, 2))
print(enter_2(1, 'hello'))

