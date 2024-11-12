
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

n = len(test_list)
res= []
key_list = ["name" , "key"]

for val in range(0,n,2):
    res.append({key_list[0]:test_list[val],key_list[1]:test_list[val+1]})

print(res)

