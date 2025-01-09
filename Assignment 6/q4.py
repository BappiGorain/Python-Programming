import numpy as np

array = np.arange(1,17).reshape(4,4)

print('original array : \n',array)

array[[0,2],:] = array[[2,0],:]

print('After swapping row 0 and row 2: \n',array)

array[:,[1,3]] = array[:,[3,1]]

print('After swapping col 1 with col 3 :\n',array)

