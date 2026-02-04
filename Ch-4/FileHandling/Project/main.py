
from pathlib import Path
import os

def readFileAndFolder():
    path=Path('') # current file
    print(path)
    items=list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createFile():
    try:
        readFileAndFolder()
        name=input("Please tell your file name:-")
        p=Path(name)
        print(p)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("What you want to write in this file")
                fs.write(data)
            print("File create successfully")

        else:
            print("This file already exist")
    except Exception as e:
        print(f"An error occured as {e}")

def readFile():
    try:
        readFileAndFolder()
        name=input("which file you want to read:- ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("Read Successfully")
        else:
            print("This file not exist")
    except Exception as e:
        print(f"An error occured as {e}")

def updateFile():
    try:
        readFileAndFolder()
        name=input("tell which you want to update:-")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changine a file name")
            print("Press 2 for overwriting the data in file")
            print("Press 3 for appending some content in your file")

        res=int(input("tell your response :- "))

        if res==1:
            name2=input("Tell your new file name :-")
            p2=Path(name2)
            p.rename(p2)
        if res==2:
            with open(p,'w') as fs:
                data=input("What you want to write or overwrite:-")
                fs.write(data)
        
        if res==3:
            with open(p,'a') as fs:
                data=input("What you want to append :-")
                fs.write(data)

    except Exception as e:
        print(e)



def deleteFile():
    try:
        readFileAndFolder()
        name=input("Which file you want to delete:-")
        p=Path(name)

        if p.exists and p.is_file():
            os.remove(p)
            print("File delete successfully")
        else:
            print("No such file exist")
    except Exception as e:
        print(e)
            

        
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check=int(input("Please tell ur response:-"))

if check==1:
    createFile()
if check==2:
    readFile()
if check==3:
    updateFile()
if check==4:
    deleteFile()
