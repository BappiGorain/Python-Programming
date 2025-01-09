import pandas as pd
import numpy as np

# (a) Create a Series from the list [7, 11, 13, 17]
series_a = pd.Series([7, 11, 13, 17])
print("Series (a):")
print(series_a)

# (b) Create a Series with five elements where each element is 100.0
series_b = pd.Series([100.0] * 5)
print("\nSeries (b):")
print(series_b)

# (c) Create a Series with 20 elements that are all random numbers in the range 0 to 100
series_c = pd.Series(np.random.randint(0, 101, 20))
print("\nSeries (c):")
print(series_c)

# Use the describe method to produce the Seriesâ€™ basic descriptive statistics
print("\nDescriptive statistics for Series (c):")
print(series_c.describe())

# (d) Create a Series called temperatures with specified values and indices
temperatures = pd.Series(
    [98.6, 98.9, 100.2, 97.9],
    index=['Julie', 'Charlie', 'Sam', 'Andrea']
)
print("\nSeries (d) - temperatures:")
print(temperatures)

# (e) Form a dictionary from the names and values in Part (d), then use it to initialize a Series
temp_dict = temperatures.to_dict()
series_e = pd.Series(temp_dict)
print("\nSeries (e) initialized from dictionary:")
print(series_e)
