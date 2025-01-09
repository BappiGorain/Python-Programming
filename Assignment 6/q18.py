import pandas as pd

data = {
    'column1' : [1,2,3],
    'column2'  : ['A','B','C'],
    'column3' : ['Apple','Bat','Cat']
        }

df = pd.DataFrame(data)
print(df)


first_column = df.iloc[:,0]
print(first_column)