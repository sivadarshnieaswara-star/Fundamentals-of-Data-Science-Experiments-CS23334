# Exp No: 5 - Data Collection and Initial Exploration (PIMA Indian Diabetes dataset)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Collection - load the dataset
db = pd.read_csv("../data/diabetes.csv")

# Display the first few rows
print(db.head())

# 2. Initial Exploration - dataset structure and summary statistics
print(db.info())
print(db.describe())

# Visualize the distribution of each feature
db.hist(bins=50, figsize=(20, 15))
plt.show()

# Pairplot to visualize relationships
sns.pairplot(db)
plt.show()
