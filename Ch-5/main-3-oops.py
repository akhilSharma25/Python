
# 4 pillar

# Inheritance

# class Parent:

#     a=12


#     def hello(self):
#         print("Hello i m a parent")


# class Child(Parent):

#     def hello(self):
#         print("Child")

# c=Child()
# c.hello()



# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"Hello my name is {self.name}")

# class Human(Animal):
#     # now parent constructor works as child consrtuctor
#     pass


# person1=Human("Akhil")
# person1.show()
# person2=Human("Rahul")
# person2.show()




# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         # print(f"Hello my name is {self.name} {self.age}") # y reccomend ni h in this case
#           print(f"Hello my name is {self.name}")

# class Human(Animal):
#        def __init__(self,name,age):
#         super().__init__(name) # target super class
#         self.age=age

#        def disp(self):
#             print(f"{self.name} {self.age}")

# person1=Human("Akhil",40)
# # person1.show()
# person1.disp()





# multiple inheritance
class A:
    name1="Lion"

    def __init__(self,name):
        pass

class B:

    name2="Hello"
    
    def __init__(self,name,age):
        pass

class C(A,B):
    name3="Don"

# c=C()
# print(c.name1)
# print(c.name2)
# print(c.name3)

c=C("Ak") # based on inheritance jo phela inherit(A,B) hoga uska constructor use hoga 


# Multilevel

class Factory:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips


class DelhiFactory(Factory):
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color=color

class PuneFactory(DelhiFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets=pockets

    
        
p=PuneFactory("Leather",4,"Red",4)
    








