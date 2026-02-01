
#? List is mutable ,duplicate,hetergenous,Orderes perserved 
# same indexing or slicing concept here

a=[12,13,14,15,9,True,"lo"]

a[0]=10 #MUTABLE
print(a[6])
print(a[0:4:1])

#!Traversing

#?first way using index
# for i in range(len(a)):
#     print(a[i])

#? Second way direcly on value
for i in a:
    print(i) # drawback only access value not index

