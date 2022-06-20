class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    # methods
    # getters and setter; preserve internal data representation
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    
    # override inherited methods
    def __add__(self, other):
        newNum = (self.getNum() * other.getDen()) + (other.getNum() * self.getDen())

        newDen = self.getDen() * other.getDen()

        return Fraction(newNum, newDen)

x = Fraction(1,2)

print(x)
print(x.getNum())
print(x.getDen())

y = Fraction(2,3)
print(y)
print(y.getNum())
print(y.getDen())

print(x + y)