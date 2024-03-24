import numpy as np

first_array = np.array([1, 3, 5, 7])
second_array = np.array([2, 4, 6, 8])

# Using the * operator
result1 = first_array * second_array
print("Using the * operator:", result1)

# Using the multiply() function
result2 = np.multiply(first_array, second_array)
print("Using the multiply() function:", result2)
