# Exp No: 14 - Understand feature scaling
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

df = pd.read_csv('../data/pre-process_datasample.csv')
print(df)
print(df.head())

df['Country'] = df['Country'].fillna(df.Country.mode()[0])
features = df.iloc[:, :-1].values
label = df.iloc[:, -1].values

age = SimpleImputer(strategy="mean", missing_values=np.nan)
Salary = SimpleImputer(strategy="mean", missing_values=np.nan)
age.fit(features[:, [1]])
Salary.fit(features[:, [2]])

features[:, [1]] = age.transform(features[:, [1]])
features[:, [2]] = Salary.transform(features[:, [2]])
print(features)

oh = OneHotEncoder(sparse_output=False)
Country = oh.fit_transform(features[:, [0]])
print(Country)

final_set = np.concatenate((Country, features[:, [1, 2]]), axis=1)
print(final_set)

sc = StandardScaler()
sc.fit(final_set)
feat_standard_scaler = sc.transform(final_set)
print("Standard Scaler:\n", feat_standard_scaler)

mms = MinMaxScaler(feature_range=(0, 1))
mms.fit(final_set)
feat_minmax_scaler = mms.transform(final_set)
print("MinMax Scaler:\n", feat_minmax_scaler)
