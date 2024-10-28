num_list  = [1,2,3,4,5,6]

num = 8

for i in range(0,len(num_list)):
    if num_list[i] == num:
        print("Element found at index", i)
        break

print("Element no found in the list")

