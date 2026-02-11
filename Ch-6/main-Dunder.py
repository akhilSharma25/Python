
#Dunder method are special method in python that start and end with double underscore __init__ ,__str__
#Dunder method called automatically ,they are automatically invoked by the interpreter whenever you use specific symbols or functions.
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):# jb hum obj print krte toh y return ho jyga instead of location
        return "Hello how are u"
    
    def __add__(self,other):
        return f"Sum of ages are {self.age + other.age}"

obj=Animal("Lion",1)
obj1=Animal("Ak",2)

print(obj)
print(obj+obj1)