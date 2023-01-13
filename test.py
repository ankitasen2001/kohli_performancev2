import numpy as np

arr = np.array(
    [1,2,4]
)

print(arr,type(arr))
print("shape of the array:",arr.shape)

arr2D = np.array([
    [1,2],
    [4,5],
    [6,7]
])


print(arr2D)
print(
    arr2D[0,0],arr2D[0,1]
)

print(
    arr2D[0,1],arr2D[1,1]
)


print(
    arr2D[2,0],arr2D[2,1]
)

arr3D = np.array([
    [
       [1,2,3],
       [4,5,6],
       [3,9,7]
    ],
    [
       [1,4,7],
       [6,8,9],
       [5,8,9]
    ],
    [      
      [4,7,8],
      [5,7,8],
      [9,9,8]
    ]
])

print(arr3D)
print(arr3D[0])
print(arr3D[0,0])
print(arr3D[0,0,0])

arr2D = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

arr2D[0,1] =7
print(arr2D)

zeros = np.zeros((4,5))
print(zeros)
print(type(zeros))

ones = np.ones((3,))
print(ones)

consts = np.full((3,3),9)
print(consts)


rand =np.random((4,4))
print(rand)