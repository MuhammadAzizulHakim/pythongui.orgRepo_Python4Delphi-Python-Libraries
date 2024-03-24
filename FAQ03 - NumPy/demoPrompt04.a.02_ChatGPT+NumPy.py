import numpy as np

first_array = np.array([3, 9, 27, 81])
second_array = np.array([2, 4, 8, 16])

# Using the - operator
result1 = first_array - second_array
print("Using the - operator:", result1)

# Using the subtract() function
result2 = np.subtract(first_array, second_array)
print("Using the subtract() function:", result2)
