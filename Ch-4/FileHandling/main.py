
# p=open('main.py')
# print("Hello")
# print(p.read())

#? open --> 4 mode
# 'r' Read(default) -> file must exit 
# 'w' Write-create files or overwrites
# 'a' Append-adds to end of file
# 'x' Create-creates a new file

# r=open('Hello.txt','w')
r=open('Hello.txt','a')

# r.write("Hello this akhil and I am Software Engineer")
r.write("/n Become Full Stack Developer")
r.close()