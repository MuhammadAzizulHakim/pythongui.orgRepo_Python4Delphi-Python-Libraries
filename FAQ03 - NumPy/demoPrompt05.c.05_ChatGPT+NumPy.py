import numpy as np

# Create a matrix
matrix = np.array([[1, 2], [3, 4]])

# Compute the Singular Value Decomposition (SVD) of the matrix
U, S, VT = np.linalg.svd(matrix)

print("U:", U)
print("S:", S)
print("VT:", VT)
