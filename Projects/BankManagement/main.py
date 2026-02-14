
#Bank Account
#Depost Money
#WithDraw Money
#Details
#Update Details
#Delete Account

import json
import random
import string
from pathlib import Path

class Bank:
    database=Path(__file__).parent / 'data.json'
    data=[] # dummy data
    try:
        if Path(database).exists():
            with open(database) as fs:
                content=fs.read()
                data=json.loads(content) if content else []
        else:
            print("No such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")
        data=[]

    @staticmethod
    def __update():

        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerat(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        nums=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$^%&*",k=1)
        id=alpha+nums+spchar

        random.shuffle(id)
        return "".join(id)
        
    def Createaccount(self):
        
        info={
            "name":input("Tell your name :- "),
            "age":int(input("Tell your age :- ")),
            "email":input("Tell your email"),
            "pin":int(input("Enter your 4 number pin :- ")),
            "accountNo":Bank.__accountGenerat(),
            "balance":0
        }

        if info['age']<18 or len(str(info['pin']))!=4:
            print("Sorry you cannot create your account")
        else:
            for i in info:
                print(f"{i} : {info[i]}")
            
            print(f"Please note down your account number")
            Bank.data.append(info)
            Bank.__update()
     
            print("Account has been created Successfully")

    def depositMoney(self):
        accNumber=input("Please tell your account number :- ")
        pin=int(input("Tell your Pin"))




user=Bank()

print("Press 1 for creating an account ")
print("Press 2 for Deposit the money in the bank")
print("Press 3 for Withdraw the money")
print("Press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check=int(input("Tell your response :- "))

if check==1:
    user.Createaccount()
if check==2:
    user.depositMoney()

