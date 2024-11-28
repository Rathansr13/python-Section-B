from collections import Counter

input_list = [1, 2, 2, 5, 8, 4, 4, 8]

l1 = []

count = 0

for item in input_list:
    if item not in l1:
        count+=1
        l1.append(item)

print(count)


#Using Counter objects

con = Counter(input_list)
print(con)

key_list  = con.keys()

print(f"THe len of Unique elements in the list is = {len(key_list)}")


for idx in con:
    if con.keys()>=2:
        print(f"duplicate element in {idx}")