# create a class
class Dog(object):
    def __init__ (self, name, age, color):
        self.name = name
        self.age = age


justice =  Dog("justice", 8, "white")
print(justice.name, justice.age)

justice =  Dog(8, "sam", "white/brown") # order matters for args
print(justice.name, justice.age)

justice =  Dog("justice", 8) # breaks; must upply all parameters for init
print(justice)