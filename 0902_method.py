class Coordinate(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    # self returns to an instance
    def distance(self, other): 
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


c = Coordinate(3,4)
origin = Coordinate(0,0)

# Calling Methods

# conventional 
print(c.distance(origin))
# object on which to call method
# inherits the distance from the class definition, automatically uses c as the first argument

# name of a class; 
print(Coordinate.distance(c, origin))
# using class to get to method  must provide both arguments
# get the value of Coordinate (a frame), looks up the value associated with distance(a procedure), then invokes it; requires two arguments
