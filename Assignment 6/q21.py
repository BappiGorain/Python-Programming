import pandas as pd

l1 = ['cry','apple','orange','sky','banana']

ser1 = pd.Series(l1) 

print(ser1)

l2 = []
vowel = ['a','e','i','o','u']
for ele in ser1:
    for v in ele:
        if v in vowel:
            l2.append(ele)
            break

ser2 = pd.Series(l2)
print(ser2)


l3 = []
for ele in ser1:
    if ele[0] in vowel:
        l3.append(ele)

ser3 = pd.Series(l3)
print(ser3)