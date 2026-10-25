# Exp No: 11 - Understand pandas library use cases in Data Science
import numpy as np
import pandas as pd

list = [[1, 'Smith', 50000], [2, 'Jones', 60000]]

df = pd.DataFrame(list)
print(df)

df.columns = ['Empd', 'Name', 'Salary']
print(df)

df.info()

df = pd.read_csv("../data/50_Startups.csv")
df.info()
print(df.head())
print(df.tail())

df = pd.read_csv("../data/employee.csv")
print(df.head())
print(df.tail())
df.info()

print(df.salary)
print(type(df.salary))
print("Mean:", df.salary.mean())
print("Median:", df.salary.median())
print("Mode:\n", df.salary.mode())
print("Variance:", df.salary.var())
print("Std:", df.salary.std())

print(df.describe())
print(df.describe(include='all'))

empCol = df.columns
print(empCol)

emparray = df.values
print(emparray)

employee_DF = pd.DataFrame(emparray, columns=empCol)
print(employee_DF)
