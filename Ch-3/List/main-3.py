
#1 Print positive and negative ele of an list

# li=[1,-1,2,-2,3,-3,4,-4]

# li.sort()
# for i in li:
#     print(i)
  
#2 average
# li=[1,2,3,4,5]

# sum=0
# for i in range(len(li)):
#     sum=sum+li[i]

# avg=(sum)/len(li)
# print(avg)

#3 find greatest element and print index too

# li=[4,1,2,5,6,9]
# maxi=li[0]
# index=0
# for i in range(len(li)):
#     # maxi=max(maxi,li[i]) # same logic
#     if(li[i]>maxi):
#         maxi=li[i]
#         index=i

# print(maxi,i)

#5 check list is sorted or not

# li=[4,1,2,5,6,9]
li=[1,2,3,4,9]
for i in range(len(li)-1):
    if li[i]<li[i+1]:
        continue
    else:
        print("List is not sorted")
        break
else:
    print("Your list is sorted")
       