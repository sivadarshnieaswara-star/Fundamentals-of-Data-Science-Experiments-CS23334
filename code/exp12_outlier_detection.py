# Exp No: 12 - Detect outliers in a given data set
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# sample calculation for low range(lr), upper range(ur), percentile
array = np.random.randint(1, 100, 16)  # randomly generate 16 numbers between 1 to 100
print("array:", array)

print("mean:", array.mean())
print("25th percentile:", np.percentile(array, 25))
print("50th percentile:", np.percentile(array, 50))
print("75th percentile:", np.percentile(array, 75))
print("100th percentile:", np.percentile(array, 100))


# outliers detection
def outDetection(array):
    sorted(array)
    Q1, Q3 = np.percentile(array, [25, 75])
    IQR = Q3 - Q1
    lr = Q1 - (1.5 * IQR)
    ur = Q3 + (1.5 * IQR)
    return lr, ur


lr, ur = outDetection(array)
print("lr, ur:", lr, ur)

sns.displot(array)
plt.show()

sns.histplot(array, kde=True, stat='density')  # replacement for deprecated sns.distplot
plt.show()

new_array = array[(array > lr) & (array < ur)]
print("new_array:", new_array)

sns.displot(new_array)
plt.show()

lr1, ur1 = outDetection(new_array)
print("lr1, ur1:", lr1, ur1)

final_array = new_array[(new_array > lr1) & (new_array < ur1)]
print("final_array:", final_array)

sns.histplot(final_array, kde=True, stat='density')
plt.show()
