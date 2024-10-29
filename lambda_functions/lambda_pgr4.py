even_item_list  = [lambda arg=i : arg*2 for i in range(1,5)]

for item in even_item_list:
    print(item())