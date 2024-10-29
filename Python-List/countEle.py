from collections import Counter
#Count of ele in list using count method
list1  = [1,3,4,5,5,8,9,4,6,6,7,8]

num = 4

count_num  = list1.count(num)

print(count_num)


#Count of ele in the list using for-loop
count_val = 0

for val in list1:

    if val == num:

        count_val+=1
print(count_val)

#Count of ele in the list using Counter object

count_val = 0

count_val = Counter(list1)

print(count_val[num])