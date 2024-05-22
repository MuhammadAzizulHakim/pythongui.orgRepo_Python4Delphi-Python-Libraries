import numpy as np

# Create a 3-dimensional array with numbers from 0 to 29
a = np.arange(30).reshape(2, 3, 5)

# Print the array and its properties
print("Array:")
print(a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Data type:", a.dtype.name)
print("Item size:", a.itemsize)
print("Number of elements:", a.size)

# Fill a matrix with random integer values
rng = np.random.default_rng()
matrix = rng.integers(low=0, high=100, size=(3, 3))

# Find max, min, and sum
print("Matrix:")
print(matrix)
print("Max element:", np.max(matrix))
print("Min element:", np.min(matrix))
print("Sum of elements:", np.sum(matrix))
