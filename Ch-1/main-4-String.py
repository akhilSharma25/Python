
a="A"
print(ord(a)) # it return unicode or ascii code

a=65
print(chr(a))#convert into char

b="Hello Brother" 

#index start from 0 positive
#It is also start from negative but from end side

#         0 1 2 3 4 5 6
#         B r o t h e r
#        -7-6-5-4-3-2-1

print(b[-1])
print(b[-5])

#slicing

s=b[-6:-2:1]# [start:end:step]  ,end is excluded , by default step is 1 [3:4 ]
print(s)

print(b[6:9:1])
print(b[:]) # full string
print(b[:5])



