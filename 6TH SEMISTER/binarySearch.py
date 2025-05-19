import numpy as np

np.random.seed(10)

def BSearch(data,key):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low+high)//2
        if data[mid] == key:
            return mid
        elif data[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1


data = np.random.randint(10,91,15)
data.sort()
print(data)
key = 50
print(BSearch(data,key))  # Output: 10


