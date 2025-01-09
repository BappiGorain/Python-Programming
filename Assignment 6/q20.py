import pandas as pd

series1 = pd.Series([1,1,3,7,88,12,88,23,3,1,9,0])

pos = 0
si = 0
li = 0
smallest = 100000000
largest = 0

for e in series1:
    if  e < smallest:
        si = pos
        smallest = e
    if e > largest:
        li = pos
        largest = e
    pos+=1

print("minimum number first index : ",si)
print("maximum number last index : ",li)