j_angry = True
s_angry = False
flag = False

if j_angry == True and s_angry == True:
    flag = True
elif j_angry == True or s_angry == True:
    flag = False

print(flag)
