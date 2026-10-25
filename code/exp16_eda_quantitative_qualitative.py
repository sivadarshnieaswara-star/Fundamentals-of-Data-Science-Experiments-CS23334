# Exp No: 16 - Understand EDA - Quantitative and Qualitative analysis (tips dataset)
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = pd.read_csv('../data/tips.csv')  # same as sns.load_dataset('tips')
print(tips.head())

sns.displot(tips.total_bill, kde=True)
plt.show()

sns.displot(tips.total_bill, kde=False)
plt.show()

sns.jointplot(x=tips.tip, y=tips.total_bill)
plt.show()

sns.jointplot(x=tips.tip, y=tips.total_bill, kind="reg")
plt.show()

sns.jointplot(x=tips.tip, y=tips.total_bill, kind="hex")
plt.show()

sns.pairplot(tips)
plt.show()

print(tips.time.value_counts())

sns.pairplot(tips, hue='time')
plt.show()

sns.pairplot(tips, hue='day')
plt.show()

sns.heatmap(tips.corr(numeric_only=True), annot=True)
plt.show()

sns.boxplot(tips.total_bill)
plt.show()

sns.boxplot(tips.tip)
plt.show()

sns.countplot(tips.day)
plt.show()

sns.countplot(tips.sex)
plt.show()

tips.sex.value_counts().plot(kind='pie')
plt.show()

tips.sex.value_counts().plot(kind='bar')
plt.show()

sns.countplot(tips[tips.time == 'Dinner']['day'])
plt.show()
