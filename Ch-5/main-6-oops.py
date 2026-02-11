
# abstraction
#abstraction does not exist in python but we can achieve using library

from abc import ABC,abstractmethod

class abs(ABC):
    # @abstractmethod
    # def perimeter(self):
    #     pass

    @abstractmethod
    def area(self):
        pass

class Square(abs):

    def __init__(self,side):
        self.side=side
    
     
    def area(self):
        print("area")

class Circle(abs):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        print("area")
    
    

obj=Circle(2)
obj.area()