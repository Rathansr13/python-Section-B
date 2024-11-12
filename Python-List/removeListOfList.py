list1 = [1,4,5,[],5,6,8,0 ,[],[],[]]

res = [val for val in list1 if val!=[]]

print(res)


#Using filter method
res = list(filter(lambda x : x!=[],list1))

print(res)