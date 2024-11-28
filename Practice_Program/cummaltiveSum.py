numbers = list(map(int,input().split()))

sum = 0

for val in numbers:
    if val < 0:
        sum=0
    else:
        sum+=val

print(f"The sum of all digits is {sum}")