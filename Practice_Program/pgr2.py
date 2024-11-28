a=int(input("enter the number"))
b=int(input("enter the number"))
flag=False
if a<0 or b<0:
    flag=False
if a<0 and b<0:
    flag=True
else:
    flag=True
print(flag)
