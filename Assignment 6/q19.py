import pandas as pd

s1 =pd.Series([1,2,3,4,2])
s2 =pd.Series([3,4,5,6])

print(s1)

l=[]
for e in s1:
    if e not in s2:
        l.append(e)
print(l)