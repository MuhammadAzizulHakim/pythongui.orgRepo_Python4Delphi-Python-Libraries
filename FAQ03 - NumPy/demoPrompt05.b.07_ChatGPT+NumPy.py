import numpy as np

A = np.array([[1, 2, 3],
              [2, 3, 4],
          	  [3, 4, 5]])

rank = np.linalg.matrix_rank(A)

print("Matrix rank:", rank)
