# SUBSTITUTION PRINCIPLE
# - important attributes of superclass should be supported by the subclass

class Person(object):
    def __init__(self, name):
        self.name = name
        self.lastName = name.split(' ')[-1]
    
    def __str__(self):
        return self.name

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def getLastName(self):
        return self.lastName

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(MITPerson):
    pass

class UnderGrad(Student):
    pass

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)