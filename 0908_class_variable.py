class Animal(object): 
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return "animal: " + str(self.name) + " : "+str(self.age)
 
    def set_name(self, newname=""):
        self.name = newname

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    

    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2


hops = Rabbit(1)
hops.set_name("hops")

bugs = Rabbit(0)
bugs.set_name("bugs")

lola = Rabbit(0)
lola.set_name("lola")

print(hops.get_rid())
print(bugs.get_rid())
print(lola.get_rid())

