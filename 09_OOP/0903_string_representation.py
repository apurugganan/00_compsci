class Coordinate(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __str__(self):
        return "whatever you like" # needs to be a string

c = Coordinate(2,3)
print(c)