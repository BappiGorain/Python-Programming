import numpy as np

arr = np.arange(1,16).reshape(3,5)
print(arr)

print(arr[1])
print(arr[:,4])
print(arr[0:2,:])
print(arr[:,1:4])
print(arr[1,3])

row = [1,2]
column = [0,2,4]

select_element = arr[np.ix_(row,column)]

print(select_element)