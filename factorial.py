num = 5

def fact(num):
    result = 1
    while num >= 1:
        result = result*num
        num-=1
    return result
    
res = fact(num)
print(res)