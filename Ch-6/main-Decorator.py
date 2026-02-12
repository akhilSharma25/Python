

# A decorator is a function that modifies or enhances another function/class without permanently changing it.

# @property is a decorator that allows you to access a method like an attribute (without parentheses).

# class Animal:
#     @property
#     def show(self):
#         print("Hello are u ")

# obj=Animal()
# obj.show # without () this call


# how to create decorator

# def decorate(func):# it take hello func as parameter
#     def wrapper():
#         print("Hey bhai this is wrapper")
#         func()# it call hello()
#         print("After")
#     return wrapper # y call krega

# @decorate
# def hello():
#     print("Hello")

# hello()


def decorate(func):# it take hello func as parameter
    def wrapper(*a,**k):
        print("the addition to your numbers are")
        func(*a,**k)# it call hello()
        print("thank u")
    return wrapper # y call krega

@decorate
def addition(*a,**b):
    print(f"Your total is {a} {b}")

addition(2,3,4,5,6,6,5)
