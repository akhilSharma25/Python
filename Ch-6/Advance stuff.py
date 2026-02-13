
# **comprehensions
# Creates a list of even numbers from 1 to 20 using list comprehension
# Prints the list of even numbers
l=[i for i in range(1,21) if i%2==0]
print(l)

u={i:i**2 for i in range(1,10)}
print(u)

# More examples of comprehensions

# Set comprehension - removes duplicates
s={i%3 for i in range(1,10)}
print(s)

# List comprehension with condition
evens_squared=[x**2 for x in range(1,11) if x%2==0]
print(evens_squared)

# Nested list comprehension
matrix=[[i*j for j in range(1,4)] for i in range(1,4)]
print(matrix)

# Dictionary comprehension with condition
filtered_dict={k:v for k,v in enumerate(range(10,15)) if k%2==0}
print(filtered_dict)

# String comprehension (list of characters)
chars=[c for c in "hello" if c!='l']
print(chars)

#!lambda function
# Lambda is a small anonymous function with no name, defined using 'lambda' keyword
# Syntax: lambda arguments: expression (takes arguments and returns a single expression result)
# Example: square = lambda x: x**2; print(square(5)) outputs 25

# def add(a,b):
#     print(a+b)

# add(1,2)

# add=lambda a,b: a+b
# print(add(1,2))

# m=lambda a:"even" if a%2==0 else "odd"
# print(m(2))


#lambda use hota map filter 
#? Map ,filter and zip 
#Map-> it is usedd for applying a function to multiple items,It takes a list(or any sequence),perfrom some calcualtion on list and gives u new list

a=[1,3,4,5]
doubled=map(lambda i: i*2,a) # it return object so  u need convert into list
print(list(doubled))

#Filter -> filter out the stuff, takes a list/sequence and filters elements based on a condition
# Returns a new filter object containing only elements where the function returns True ,it works on true or false condition

def even(x):
    if x%2==0:
        return True
    else:
        return False

a=[1,2,3,4,5,6,7,8,9]
res=filter(even,a)# return obj
print(list(res))






