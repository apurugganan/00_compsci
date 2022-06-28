class Animal(object): 
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return "animal: " + str(self.name) + " : "+str(self.age)
 
    def set_name(self, newname=""):
        self.name = newname

# Working with types
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

    #  WORKING WITH TYPES
    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid

        parent_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid

        return parents_same or parent_opposite


bugs = Rabbit(2)
bugs.set_name("bugs")

lola = Rabbit(2)
lola.set_name("lola")

hops = bugs + lola
hops.set_name("hops")
print(hops)

bunnie = Rabbit.__add__(lola, bugs)
bunnie.set_name("bunnie")
print(bunnie)

print(hops == bunnie)