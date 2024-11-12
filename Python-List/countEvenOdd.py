l1 = [1,2,3,4,5,6,7,8,9]

even_count  = 0
odd_count = 0

for val in l1:
    if val%2 == 0:
        even_count+=1
    else:
        odd_count+=1


print(odd_count , even_count)