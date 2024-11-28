a=int(input("enter the number"))
b=int(input("enter the number"))
opr=str(input("enter"))
print(opr[0:3])
if str (opr[0:3])=="add":
        print(a+b)
elif str(opr[0:3])=="sub":
    print(a-b)
elif str(opr[0:3])=="mul":
    print(a*b)
else:
    print("invalid")
