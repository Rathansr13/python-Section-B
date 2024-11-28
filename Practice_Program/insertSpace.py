

list_x = input("Enter the string")


list_con = list(list_x)

for i in range(len(list_con)-1,0,-1):
    list_con.insert(i,'*')
    
print(list_con)