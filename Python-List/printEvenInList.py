l1 = [1,2,3,4,5,6,7,8,9]
res = []
for val in l1:
    if val%2 == 0:
        res.append(val)
print(res)

#Using List Comprehension

res  = [val for val in l1 if val%2==0]
print(res)


#Using filter method 

res = list(filter(lambda x : x % 2 == 0, l1))
print(res)