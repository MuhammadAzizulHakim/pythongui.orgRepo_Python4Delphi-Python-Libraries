import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result_matmul = np.dot(matrix1, matrix2)
# Alternatively, you can use the @ operator
result_matmul = matrix1 @ matrix2

print("Matrix Multiplication:\n", result_matmul)
