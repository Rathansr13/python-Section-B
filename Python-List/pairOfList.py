test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

res = []

for idx in test_list:
   val = idx[-1]
   for ele in idx:
      if ele == val:
         continue
      res.append(list([ele,val]))
print(res)