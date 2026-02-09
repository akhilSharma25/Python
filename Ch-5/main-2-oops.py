
class Animal:
    name="lion" # class attr

    def __init__(self,age):
        self.age=age # instance attri
    
    @classmethod
    def hello(cls): # class method
        #cls target animal class
        pass

    @staticmethod
    def static_method():
        print("Hello")

    def show(self): # age hmnae yyha self d diya mtlb y instance method hi h
        # agr yhe method m self pass ni kroge toh error aaayga
        pass

obj=Animal(10)
obj.hello()        
obj.static_method()
Animal.static_method()
Animal.hello()