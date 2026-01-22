
#integer
a=12
print(type(a))

#Float for real value like decimal or fraction
b=1.2
d=12/3
print(d)
print(type(d))

#complex
v=34j # j is important here to define the variable as comples number
print(type(v))

#String '' ""
name='Ram'
name="Ram Ram"
print(type(name))

#Boolean
t=True
f=False
print(t)


# Type Conversion
#Explicit
var=10
print(str(var))  

print(float(var))
print(int("20"))

d="A"
#!print(int(d)) #invalid  ,str To convert into interger or float string must be intger "28"


b=12
print(bool(b))
print(bool("G")) 

#it is based on truthy or falsely value
#! false ,0,0.0 ,"",[],{},() all these give false value

#Implicit
a=10/3
print(a)