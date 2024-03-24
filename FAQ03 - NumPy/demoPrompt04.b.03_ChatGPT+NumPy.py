import numpy as np

# Create two NumPy arrays for matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result_matmul = np.dot(matrix1, matrix2)

# Matrix inversion
result_inv = np.linalg.inv(matrix1)

# Matrix transpose
result_transpose = np.transpose(matrix1)

print("Matrix Multiplication:\n", result_matmul)
print("Matrix Inversion:\n", result_inv)
print("Matrix Transpose:\n", result_transpose)
