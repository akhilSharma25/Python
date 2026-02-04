
# print("Hello World" # Error

# if a==12:
# print("Hello") #indentation error


#Exception-> unexpected error 
# a=int(input("Tell ur number :- "))
# print(10/a) # if a is 0 then raise zerodivision error
# print("Done") # this line will never run


'''
#! Try -> wrap the block of code that might cause an exception
#! except -> handle the exception if it occurs
#! else -> Run code only if no exception occurs
#! finally -> Run code no matter what ,whether exception occur or not
#! raise -> manually throw an exception
'''


# try:
#     print(10/a) 
# except ZeroDivisionError as e:
#     print("Sorry you can not divide by 0",e)

# try:
#     print(10/a) 
# except Exception as err:
#     print("Sorry! It is not allowed",err)
# else:
#     print("Done no error")
# finally:
#     print("Bye")



# a=(input("Tell ur str :- "))

# try:
#     print(10/a) # divide by string
# except Exception as e:
#     print(e)



age=int(input("Tell ur age:-"))

try:
    if age<10 or age>18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")
except (ValueError, TypeError) as e:
    print(e)
except Exception as e:
    print(e)

finally:
    print("the club will start soon")
    





