
def hello():
    print("Hello Dosto!")

hello()

#parameter
def add(a,b):
    print("Addition is",a+b)

add(2,4)

#type of argument

#1 positional argument
# def add(a,b):
#     print("Addition is",a+b)

# add(2,4)

# 2 keyword argument

def bye(name,age):
    print(f"Your name is {name} and your age is {age}")

bye(age=22,name="Akhil")

# 3 DEfault argument

def sum(a,b=45):
    return a+b

sum(2)
a=sum(2,3)
print(a)



