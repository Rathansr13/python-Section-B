list1 = [12,213,56,78]


res  = []

print(f"Original list = {str(list1)}")

for val in list1:
    sum_val = 0 
    for i in str(val):
        sum_val+=int(i)
    res.append(sum_val)

print(f"Sum of the digit in the list {res}")