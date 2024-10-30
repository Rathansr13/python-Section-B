list1  = [1,2,3,4,5,5,6]

largest  = list1[0]

for val in list1:
    if val > largest:
        largest = val

print(f"Largest in the list = {largest}")