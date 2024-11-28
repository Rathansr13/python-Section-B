simple_str=str(input("enter a random string"))
random_str=simple_str.lower()
vowels="a,e,i,o,u"
count=0
for val in random_str:
 if val in vowels:
     count+=1
print(count)
