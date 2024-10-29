import numpy as np

list1 = [1,2,3,4,5,6,7,8,]

#Using for loops to sum and avg

print("Using Loops")

sum_val = 0

for val in list1:
    sum_val+=val

print(f"Sum of the list {sum_val}")

print(f"Average of the list {sum_val/len(list1)}")

print()

#Using Sum method for sum and avg

print("Using the sum method")

sum_val = sum(list1)

avg = sum_val/len(list1)

print(f"Sum of the list using sum method={sum_val}")

print(f"Average of the list={avg}")


#using the numpy package
print("Using the numpy package")

sum_val = np.sum(list1)

avg = np.average(list1)

print(f"Sum of the list using numpy module functions = {sum_val}")

print(f"Average of the list using numpy = {avg}")