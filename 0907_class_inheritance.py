
class Animal(object): 
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return "animal: " + str(self.name) + str(self.age)
 
    def set_name(self, newname=""):
        self.name = newname

class Cat(Animal):
    # new functionality
    def speak(self):
        print("meow")

    # override functionality 
    def __str__(self):
        return "cat: " + str(self.name) + ":" + str(self.age)


# USE SUPER CLASS TO INITIALIZE AN INSTANCE
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

class Student(Person):
    def __init__ (self, name, age, major = None):
        Person._init(self, name, age)
        self.major = major

