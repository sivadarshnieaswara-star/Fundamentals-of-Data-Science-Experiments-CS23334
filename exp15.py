# Exp No: 15 - Understand data preprocessing in Data Science
import numpy as np
import pandas as pd

df = pd.read_csv("data/pre-process_datasample.csv")
print(df)

df.info()

print(df.Country.mode())
print(df.Country.mode()[0])
print(type(df.Country.mode()))

df['Country'] = df['Country'].fillna(df.Country.mode()[0])
df['Age'] = df['Age'].fillna(df.Age.median())
df['Salary'] = df['Salary'].fillna(round(df.Salary.mean()))
print(df)

print(pd.get_dummies(df.Country))

updated_dataset = pd.concat([pd.get_dummies(df.Country), df.iloc[:, [1, 2, 3]]], axis=1)
print(updated_dataset)

df.info()

updated_dataset['Purchased'] = updated_dataset['Purchased'].replace(['No', 'Yes'], [0, 1])
print(updated_dataset)
