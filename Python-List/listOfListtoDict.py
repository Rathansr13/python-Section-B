


# initializing list
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

res = dict()

for sub in test_list:
    res[tuple(sub[:2])] = tuple(sub[2:])

print(res)


#Using List comprehension

res = [(tuple(sub[:2]),tuple(sub[2:])) for sub in test_list]
print(res)