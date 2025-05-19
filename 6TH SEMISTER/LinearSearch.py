import numpy as np
np.random.seed(5)


def ls(values,target):
    for i,k in enumerate(values):
        if k==target:
            return i
    return -1


values = (np.random.randint(10,91,10))
print(values)

target = 40

print(ls(values,target))
