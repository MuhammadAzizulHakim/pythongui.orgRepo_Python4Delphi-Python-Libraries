import numpy as np

A = np.array([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]])

A_squared = np.linalg.matrix_power(A, 2)

print("A squared:")
print(A_squared)
