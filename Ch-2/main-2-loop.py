
# for loop

#Range function
# range(1,20,2) # start,stop,step and stop is excluded

#for loop
a=range(1,20,1) 
# for i in a:
#      print("A")
# for i in range(1,10):
#      print("A")

# for i in range(10): # here defautl start value is 0 and step is 0 and we only need to give end
#      print(i)

#reverse
# for i in range(10,0,-1):
#      print(i)

#5 table

# for i in range(1,11):
#      print(f"5 * {i} = {5*i}")


#strings
a="Akhil"
# for i in a:
#     print(i)

# for i in range(0,len(a)):
#     print(a[i])

# break 

# for i in range(0,5):
#     if i==2:
#         break
#     else:
#         print(i)
    
#continue

# for i in range(0,5):
#     if i==3:
#         continue
#     else:
#         print(i)


#else with loop

for i in range(1,6):
    if(i==4):
        print("Break statement is executed")
        break
else:
    print("Break statement is not executed")  # if statement execute in loop than else will not execute and vice versa
