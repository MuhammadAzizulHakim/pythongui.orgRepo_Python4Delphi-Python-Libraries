import numpy as np

A = np.array([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]])

det = np.linalg.det(A)

print("Determinant:", det)
