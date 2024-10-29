#using reverse methof to reverse a list
print("Using Reverse methond")
list1 = [1,2,3,4,5,6]

print(list1)

list1.reverse()

print(list1)
print()

#using slice to reverse a list

print("Using Slice method")
list1 = [1,2,3,4,5]

print(list1)

list_rev = list1[::-1]

print(list_rev)
print()

#using reversed method

print("Using Reversed method")
list1 = [1,2,3,4,5,8,9]

print(list1)

list2 = list(reversed(list1))

print(list2)
print()

#Using For-loop to reverse a list

list1 = [1,2,3,4,5,6,7,8]

print(list1)

rev_list  = []

for i in range(0,len(list1)):
    rev_list.insert(0,list1[i])

print(rev_list)
print()

#Using list comprehensions

print("Using List Comprehension")
list1 = [1,2,3,4,5,6,7,]

print(list1)

res  = [list1[i] for i in range(len(list1)-1,-1,-1)]

print(res)