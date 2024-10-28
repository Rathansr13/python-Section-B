num_list  = [1,2,3,4,5]

print(num_list)

temp = num_list[1]

num_list[1] = num_list[3]

num_list[3] = temp

print(num_list)