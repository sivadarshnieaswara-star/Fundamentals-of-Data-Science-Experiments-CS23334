# Exp No: 10 - Understand array functions in Data Science using NumPy
import numpy as np

array = np.random.randint(1, 100, 9)
print("array:", array)

print("np.sqrt(array):", np.sqrt(array))

print("array.ndim:", array.ndim)

new_array = array.reshape(3, 3)
print("new_array:\n", new_array)

print("new_array.ndim:", new_array.ndim)

print("new_array.ravel():", new_array.ravel())

newm = new_array.reshape(3, 3)
print("newm:\n", newm)

print("newm[2, 1:3]:", newm[2, 1:3])

print("newm[1:2, 1:3]:", newm[1:2, 1:3])

print("new_array[0:3, 0:0]:", new_array[0:3, 0:0])

print("new_array[0:2, 0:1]:\n", new_array[0:2, 0:1])

print("new_array[0:3, 0:1]:\n", new_array[0:3, 0:1])

print("new_array[1:3]:\n", new_array[1:3])
