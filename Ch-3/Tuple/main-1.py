
#? Tuple() is immutable ,duplicates,orderes,herterogenous

a=(1,2,3,3,4)
# a[0]=3 # immutable

print(a)
# print(type(a))

#traverse

for i in a:
    print(i)

for i in range(len(a)):
    print(i)

#method only 2 here

index=a.index(3) #Return first index of value.
count=a.count(2) # Return number of occurrences of value.
print(count,index)

# tuple unpacking

a,b,c,d=(1,2,3,4) # a=1,b=2,c=3,d=4
print(a,b,c,d)

b=(10) #(packing) u have to do like this to convert this into tuple ->(10,)
print(type(b))
b=(10,)
print(type(b))



