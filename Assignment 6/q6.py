import numpy as np

l = [2**i for i in range(6)]

array = np.array(l).reshape(2,3)
print(array)
array1 = array.flatten()

print(array1)

array.ravel()

print(array)