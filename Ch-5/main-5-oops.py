
# Encapsulation

#Everything we have done by default is public 

#Protected (_)
# class Factory:

#     _a="Pune" # protected same work as public
#     def show(self):
#         print("Hello ")
    
# class B(Factory):
#     pass

# b=B()
# b.show()

#Private(__)

class Factory:

    __a="Pune" # private we cannot access outside the class
    def __show(self):
        print("Hello ")

F=Factory()
# F.__a="Dh"
# print(F.__a)



