import copy

list1 = [1, 2, 3, 5, 6, 7]

# Using Slice 
def clone_slice(list1):
    print("Using Slice")
    rev_list = list1[:]
    return rev_list

# Using extend method
def clone_extend(list1):
    print("Using extend method")
    rev_list = []
    rev_list.extend(list1)
    return rev_list

# Using copy 
def clone_copy(list1):
    print("Using copy method")
    rev_list = list1.copy()
    return rev_list

# Using Shallow copy 
def clone_shallow_copy(list1):
    print("Using the shallow copy")
    rev_list = copy.copy(list1)
    return rev_list

# Using for-loop for cloning
def clone_loop(list1):
    print("Using for-loop")
    rev_list = [val for val in list1]
    return rev_list

# Using append method
def clone_append(list1):
    print("Using append method")
    rev_list = []
    for val in list1:
        rev_list.append(val)
    return rev_list

# Test functions
print(clone_slice(list1))
print()
print(clone_copy(list1))
print()
print(clone_extend(list1))
print()
print(clone_shallow_copy(list1))
print()
print(clone_append(list1))
print()
print(clone_loop(list1))
