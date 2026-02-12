
# *args ,**kwargs


def addition(*a):# *(args) k aage jo bi likhoge bo bn jyga tuple for send accepting the multiple element or argument
    # print(sum(a))
    sum=0
    for i in a:
        sum+=i
    print(sum)


addition(1,2,3,4,4,5,6)

# **kwargs(keyword argument)

def add(**k): # dicitonary
    print(k)
    for i in k:
        print(f"{i} : {k[i]}")



add(a=1,b=2,c=5,d=5)