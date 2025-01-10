import pandas as pd

data = {'Maxine' : [1,2,3] , 'James' : [2,4,6] , 'Amanda' : [3,6,9]}

temperature = pd.DataFrame(data)
print(temperature)

temperature1 = pd.DataFrame(data,index=['Morning','Afternoon','Evening'])
print(temperature1)