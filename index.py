import numpy as np

arr= np.array([
    [5,4,3,1],
    [7,3,9,3],
    [6,4,2,4]
])

#print(arr, arr.shape)

s_arr = arr[:2 ,1:3]
#print(s_arr,s_arr.shape)
(arr)
#Extract last row and col 0,col 1
print(arr[-1, :2])
#Extract second row
print(arr[-2, :])
#extract third row
print(arr[:, 2:3])
#extract col 1 and col 2
print(arr[:,1:3])

arr = np.array([
    [5,4,3,1],
    [7,3,9,3],
    [6,4,2,4]
])

print(arr)
bool_idx = [arr > 3]
print(bool_idx)

print(arr[arr > 3])

x= np.array([
    [2,4],
    [5,3]
])
y=np.array([
    [6,7],
    [3,5]
])
print(y)
print(x+y)
print(np.add(x,y))

print(np.subtract(x,y))

print(np.multiply(x,y))
print(np.divide(x,y))

print(np.sqrt(x))

x= np.array([
    [2,4],
    [5,3]
])
y=np.array([
    [6,7],
    [3,5]
])

print(y)
v = np.array([4,5])
w = np.array([3,6])

print(x.dot(y))
print(np.dot(x,y))

print(x)
print(x.T)

u = np.array([
    [3,0,6],
    [5,9,3],
    [4,8,5]
])

print(u)
#print(u.T)

print("sum of all elements of u:",np)
print("sum of each column:", np.sum(u, axis = 0))
print("sum of all rows:", np.sum(u, axis =1))

x= np.array([
    [3,4,5],
    [2,6,3],
    [8,4,1]
])

v = np.array([1,0,1])

y = np.empty_like(x)
print(y)

for i in range(len(x)):
    y[i,:] = x[i,:] + v

print(x)
print(y)

#mathamatical approach
stacked_v = np.tile(v,(3,1))
print(stacked_v)

print(x + stacked_v)

print(x+v)




x =np.array([1,2,3])

print(x)
print(np.reshape(x,(3,1)))

x = np.array([
    [3,4,5],
    [2,6,3],
])
print(x)
print(np.reshape(x, (3,2)))