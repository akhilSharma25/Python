
#? Set is mutable ,not duplicate ,unordered(mean no index concept),heterogeneous(It can store some immutable data type like string num,tuple not everything(list,dict)) 
s={1,2,8,"hello",3,4,4}
# print(s)

# a=12
# print(hash(a))
# print(hash("Hello"))

#? traverse using only value 
# for i in s:
#     print(i) # random value

#?Method

s.add(10)
# print(s)

# s.remove(2)
# print(s)
# s.pop() # random pop
# print(s)


# s.clear() # remove all element
# print(s)


A={1,2,3}
B={3,4,5}
# union_set=A.union(B) # A|B
# print(union_set)
intersect_set=A.intersection(B) # A&B
print(intersect_set) 

print(A.difference(B)) #A-B
print(B.issubset(A))
print(3 in B)

