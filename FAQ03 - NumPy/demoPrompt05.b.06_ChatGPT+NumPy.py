import numpy as np

A = np.array([[1, 2, 3],
          	  [2, 3, 4],
          	  [4, 5, 6]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
