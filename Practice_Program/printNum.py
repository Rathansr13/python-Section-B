num = int(input("enter the num"))


if num > 0:
    while num >= 0:
        print(num)
        num-=1
else:
    while num <=0:
        print(num)
        num+=1
print("result printed successfully")