name = 'bob'
fileHandle = open('hello', 'w')
fileHandle.write('hello world\n')

for i in range(2):
    name = input('Enter name: ')
    fileHandle.write("hello" + name + "\n")

fileHandle.close()