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


# look at the # of missing points in the first ten columns
missing_values_count[0:10]

# remove all the rows that contain a missing value
even_data.dropna()

# remove all columns with at least one missing value
columns_with_na_dropped = even_data.dropna(axis=1)
columns_with_na_dropped.head()

# just how much data did we lose?
print("Columns in original dataset: %d \n" % even_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

# get a small subset of the even dataset
subset_even_data = even_data.loc[:, 'Permit Number':'Permit Type'].head()
print(subset_even_data)
# replace all NA's with 0
subset_even_data.fillna(0)

# replace all NA's the value that comes directly after it in the same column, 
# then replace all the remaining na's with 0
subset_even_data.fillna(method='bfill', axis=0).fillna(0)