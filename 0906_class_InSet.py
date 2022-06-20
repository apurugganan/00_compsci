class InSet(object):
    def __init__(self):
        self.vals = []
    
    def __str__(self):
        self.vals.sort()
        result = ''
        for el in self.vals:
            result = result + str(el) + ","
        return "{" + result[:-1] + "}"
    # methods
    def insert(self, el):
        """
        Adds argument in list 
        """
        if not el in self.vals:
            self.vals.append(el)

    def isMember(self, el):
        return el in self.vals

    def remove(self, el):
        try: 
            self.vals.remove(el)
        except:
            raise ValueError(str(el) + " not found")

x = InSet()

x.insert(1)
x.insert(2)
x.insert(3)

print(x)
print(x.isMember(2))

x.remove(2)
print(x)
x.remove(2)