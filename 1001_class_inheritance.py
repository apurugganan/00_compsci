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
    

p1 = Person('Bob Aaron')
p2 = Person('Joe Baron')
p3 = Person('Tom Caron')

print(p1)
print(p2)
print( p1 < p2)



# ================ SORTING ============ 
pList = [p3, p2, p1]

# BEFORE SORT 
for person in pList:
    print('list '+ str(person))

pList.sort()

# AFTER SORT
for person in pList:
    print('list '+ str(person))


# ================ INHERITANCE ===========

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def __lt__(self, other):
        return self.idNum < other.idNum 

m4 = MITPerson('Dave Daron')
m5 = MITPerson('Eli Earon')
m6 = MITPerson('Fred Faron')

print(m4 < m5)

print(p1 < m4)
print(Person.__lt__(p1, m4))
print(p1.__lt__(m4))


# MITperson is sorted by using its own __lt__;
# __lt__ method is overrides the Person.__lt__ method
try:
    print(m4 < p1)
except: 
    print('MITPerson.__lt__() is being applied to an object without the correct attribute')


mList = [m6, m5, m4]
for person in mList:
    print(person)

mList.sort()

for person in mList:
    print(person)
