import numpy as np

x = [[1,2,3], 
     [3,4,5], 
     [6,7,8]]

y = [[1,2,3], 
     [3,4,5], 
     [6,7,8]]

res = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j]+y[i][j]

print(res)

res = np.array(x)+np.array(y)
print(res)