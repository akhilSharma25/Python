
#Dict mutable(only value change not key) ,duplicate value is allowed but key must be  unique,Order perserved,Hetergeneous
# d={} # dict

d={1:'Akhil',2:'Rahul',"B":"Bhai"}
# print(type(d))

# print(d[2])
# print(d['B'])

#method

# d.update({2:"Rama"}) #updating
# d[1]="Hey"#updating
# d[5]="Tim" # creating
# del d["B"] # deleting

# print(d.get(1,0))
# print(d.clear())
# print(d.items())
# print(d.keys())
# print(d.pop(1))
# print(d.popitem()) #last s delete whole item

#? traverse

# It only give key
# for i in d:
#     print(f"{i} :",d[i])

# for i in d.keys():
#     print(i)

# # it give value
# for i in d.values():
#     print(i)



#! deep copy

# a=[1,2,4,5]
# b=a
# b[0]=10  # change the original data , a and b point same memory location
# print(a)

#!Shallow copy

# a=[1,2,3,4,5]

# b=a.copy() 
# b[0]=10 # No changes in a 
# print(a)
# print(b)

#! same conecpt follow in dict









