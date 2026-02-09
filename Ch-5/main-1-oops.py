
# class Factory:
#     a=12 #attribute

#     def hello(self): # method
#         print("Hello")

#     # print("How are u") # only one time print when class load in memory

# # print(Factory().a)
# # Factory().hello()

# obj=Factory() #object
# print(obj.a)
# obj.hello()



class Factory:

    def __init__(self,material,zips,pockets): # constructor
        # print(self)# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
        self.material=material
        self.zips=zips
        self.pockets=pockets

    def show(self):
        print(f"Your object details are {self.material},{self.pockets},{self.zips}")

reebok=Factory("Leather",3,2)
print(reebok.material)
reebok.show()
campus=Factory("nylon",3,3)