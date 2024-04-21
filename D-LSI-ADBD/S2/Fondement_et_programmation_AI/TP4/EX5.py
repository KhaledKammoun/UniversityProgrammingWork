# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
even_data = pd.read_csv("Building_Permits.csv", low_memory=False)

# set seed for reproducibility
np.random.seed(0) 
print(even_data.head())

missing_values_count = even_data.isnull().sum()

# look at the # of missing points in the first ten columns
missing_values_count[0:10]

# how many total missing values do we have?
total_cells = np.product(even_data.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)