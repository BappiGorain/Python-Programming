import numpy as np

array1 = np.array([[0,1],[2,3]])
array2 = np.array([[4,5],[6,7]])

array3 = np.concatenate((array1,array2),axis=0)
print(array3)

array4 = np.concatenate((array1,array2),axis=1)
print(array4)

array5 = np.concatenate((array3,array3),axis=1)
print(array5)

array6 = np.concatenate((array4,array4),axis=0)
print(array6)