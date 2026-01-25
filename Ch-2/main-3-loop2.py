
# while loop

# a=1

# while a<9:
#     print("Akhil")
#     a=a+1

# a=256
# while a>0:
#     print(a%10)
#     a=a//10

#revrse number
# a=256
# copy=a
# rev=0
# while a>0:
#     rev=rev*10+(a%10)
#     a=a//10

# print("rev is ",rev)

# palindrome

# if copy==rev:
#     print("Palindrome number")
# else:
#     print("Palindrome not number")


# Random number guess game

import random

num=random.randint(1,11)
# print(num)
tries=0

while tries!=3:
    guess =int(input("Please guess your number between 1 to 11, You will get only three tries to guess the number :-"))

    if num==guess:
        print("you are right")
        break
    else:
       tries+=1
       if guess<num:
                  print("Sorry you are wrong try again Guessed number lesser than Actual Num")
       else:
            print("Sorry you are wrong try again Guessed number greater than Actual Num")

print(num)

