#find min using min function
list1 = [-1,2,3,4,5,6]

min_val = min(list1)

print("min val in the list = ",min_val)

#find the smallest using for loop

smallest = list1[0]

for val in list1:
    if val < smallest:
        smallest = val

print(f"Smallest in the given list is = {smallest}") 

