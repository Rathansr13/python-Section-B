


print("Enter the value for Set A")

A = list(map(int, input().split()))

print("Enter the value for Set B")

B = list(map(int,input().split()))

res=[]

for val_a in A:
    for val_b in B:
        res.append(tuple([val_a,val_b]))

print(f"The result is = {res}")