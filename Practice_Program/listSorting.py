


list1 = list(map(int,input().split()))
n = int(input("Enter the number of list"))

base =  len(list1)//n

extra = len(list1)%n

sub_list = []

start = 0

list1.sort()
print(list1)

for i in range(n):
    end = start+base+(1 if i<extra else 0)
    sub_list.append(list1[start:end])
    start=end

print(sub_list)