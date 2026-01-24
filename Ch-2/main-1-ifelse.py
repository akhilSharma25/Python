
#IF else

a=3

if a>10:
    print("I will do task A")   
#? recommends using 4 spaces for each level of indentation 
else:
    print("I will do task B")


# if elif else  isme s ek hi excute  hoga
# money=int(input("Enter money"))
# if money==10:
#     print("I will buy chips")
# elif money==20:
#     print("I will buy Kurkure")
# else:
#     print("I will buy toffee")


# num1=int(input("Enter num1"))
# num2=int(input("Enter num2"))

# if (num1>=num2):
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")


# name=input("Enter your name")
# age=int(input("Enter your age"))

# if(age>=18):
#     print(f"{name} is eligible for vote")
# else:
#     print(f"You are not valid voter because {name} age({age}) is less than 18")



temp=int(input("Enter today temperature"))

if(temp>=40):
    print("Very Hot")
elif(temp>=30):
    print("Hot")
elif(temp>=20):
    print("Pleasant")
elif(temp>=10):
    print("Cold")
else:
    print("Very cold")