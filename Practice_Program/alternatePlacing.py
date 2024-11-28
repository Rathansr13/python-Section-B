


random_str = list(map(str,input().split()))

x =[]
y =[]

for i in range(0,len(random_str)):
    if i%2 == 0:
        x.append(random_str[i])
    else:
        y.append(random_str[i])


x.reverse()

print(f"x = {x}")
print(f"y = {y}")