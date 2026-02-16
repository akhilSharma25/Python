
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
        pin=int(input("Tell your Pin :- "))

        userData=[i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin] # deep copy hogi ab
        if not userData:
            print("Sorry no data found")
        else:
            amount=int(input("How much you want to deposit :- "))
            if amount>10000 or amount<0:
                print("SOrry the amount is too much you can deposit below 10000 and above 0")
            else:
                # print(userData)
                userData[0]["balance"]+=amount
                Bank.__update()
                print("amount deposited successfully")

    def withdrawMoney(self):
        accNumber=input("Please tell your account number :- ")
        pin=int(input("Tell your Pin :- "))

        userData=[i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin] # deep copy hogi ab
        if len(userData)==0:
            print("Sorry no data found")
        else:
            amount=int(input("How much you want to withdraw :- "))
            if userData[0]["balance"]<amount or amount<0:
                print("Sorry! You dont have that much money")

            else:
                # print(userData)
                userData[0]["balance"]-=amount
                Bank.__update()
                print("amount withdraw successfully")

    def showDetails(self):
        accNumber=input("Please tell your account number :- ")
        pin=int(input("Tell your Pin :- "))

        userData=[i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin] # deep copy hogi ab
        if len(userData)==0:
            print("Sorry no data found")
        else:
            print("Your information are\n")
            for i in userData[0]:
                print(f"{i} : {userData[0][i]}")

    def updateDetails(self):
         accNumber=input("Please tell your account number :- ")
         pin=int(input("Tell your Pin :- "))

         userData=[i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin] 
         if len(userData)==0:
            print("Sorry no data found")
         else:
             print("You cannot change the age,account number,balance")
             print("Fill the details for chanes or leave it empty if no change ")
             newData={
                 "name":input("Please tell your name or press enter :- "),
                 "email":input("Please Tell ur new Email or press enter to skip:- "),
                 "pin":input("Enter new Pin or press enter to skip:- ")
             }

             if newData["name"]=="":
                 newData["name"]=userData[0]['name']

             if newData["email"]=="":
                 newData["email"]=userData[0]['email']

             if newData["pin"]=="":
                 newData["pin"]=userData[0]['pin']

             if newData["name"]=="":
                 newData["name"]=userData[0]['name']

             newData['age']=userData[0]['age']
             newData['accountNo']=userData[0]['accountNo']
             newData['balance']=userData[0]['balance']

             if type(newData['pin'])==str:
                 newData['pin']=int(newData['pin'])
             

             for i in newData:
                 if newData[i]==userData[0][i]:
                     continue
                 else:
                     userData[0][i]=newData[i]
            
             Bank.__update()
             print("Details updated successfully")

    def Delete(self):
            accNumber=input("Please tell your account number :- ")
            pin=int(input("Tell your Pin :- "))

            userData=[i for i in Bank.data if i['accountNo']==accNumber and i['pin']==pin] 
            if len(userData)==0:
                print("Sorry no data found")
            else:
                check=input("Press Y If you actually want to delete account or press n to skip:- ")

                if check =='n' or check=="N":
                    print("By pass")
                    pass
                else:
                    print(userData)
                    index=Bank.data.index(userData[0])
                    
                    Bank.data.pop(index)
                    print("Account Deleted Successfully ")
                    Bank.__update()


         








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
if check==3:
    user.withdrawMoney()
if check==4:
    user.showDetails()
if check==5:
    user.updateDetails()
if check==6:
    user.Delete()

