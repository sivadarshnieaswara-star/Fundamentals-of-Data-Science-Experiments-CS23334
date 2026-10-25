# Exp No: 13 - Handle missing values and inappropriate data in a given data set
import numpy as np
import pandas as pd

# Upload Hotel.csv and convert it into dataFrame
df = pd.read_csv("../data/Hotel_Dataset.csv")
print(df)

# From the dataframe identify the duplicate row (i.e row 9)
print(df.duplicated())

df.info()

# The drop_duplicates() method removes duplicate rows
df.drop_duplicates(inplace=True)
print(df)

print("len(df):", len(df))

# Reset the index
index = np.array(list(range(0, len(df))))
df.set_index(index, inplace=True)
print(index)
print(df)

# Drop the duplicate column
df.drop(['Age_Group.1'], axis=1, inplace=True)
print(df)

# Replace inappropriate (negative / out of range) values with NaN
df = df.astype({'CustomerID': float, 'Rating(1-5)': float, 'Bill': float,
                'NoOfPax': float, 'EstimatedSalary': float})
df.loc[df.CustomerID < 0, 'CustomerID'] = np.nan
df.loc[(df['Rating(1-5)'] < 1) | (df['Rating(1-5)'] > 5), 'Rating(1-5)'] = np.nan
df.loc[df.Bill < 0, 'Bill'] = np.nan
df.loc[df.EstimatedSalary < 0, 'EstimatedSalary'] = np.nan
print(df)

df.loc[(df['NoOfPax'] < 1) | (df['NoOfPax'] > 20), 'NoOfPax'] = np.nan
print(df)

print(df.Age_Group.unique())
print(df.Hotel.unique())

df['Hotel'] = df['Hotel'].replace(['Ibys'], 'Ibis')
print(df.FoodPreference.unique())
df['FoodPreference'] = df['FoodPreference'].replace(['Vegetarian', 'veg'], 'Veg')
df['FoodPreference'] = df['FoodPreference'].replace(['non-Veg'], 'Non-Veg')

# Numerical continuous -> mean, numerical discrete -> median, categorical -> mode
df['EstimatedSalary'] = df['EstimatedSalary'].fillna(round(df.EstimatedSalary.mean()))
df['NoOfPax'] = df['NoOfPax'].fillna(round(df.NoOfPax.median()))
df['Rating(1-5)'] = df['Rating(1-5)'].fillna(round(df['Rating(1-5)'].median()))
df['Bill'] = df['Bill'].fillna(round(df.Bill.mean()))
print(df)
