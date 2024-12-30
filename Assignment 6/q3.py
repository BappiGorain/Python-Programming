import numpy as np

matrix1 = np.arange(2,19,2).reshape(3,3)
matrix2 = np.arange(9,0,-1).reshape(3,3)

print(matrix1 * matrix2)