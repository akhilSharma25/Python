
#Polymorphism

#Python does not support method overloading

#!Method overriding
# class Animal:

#     def show(self):
#         print("Show 1")

   
# class Human(Animal):
#      def show(self):# overriding
#         print(f"Show 2")

# obj=Human()
# obj.show()


#! Duck Typing

class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    # This isn't a duck, but it can "quack"
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(obj):
    # We don't care about the type; we only care if it has a .quack() method
    obj.quack()

# Both work perfectly
make_it_quack(Duck())    # Output: Quack, quack!
make_it_quack(Person())  # Output: I'm quacking like a duck!
