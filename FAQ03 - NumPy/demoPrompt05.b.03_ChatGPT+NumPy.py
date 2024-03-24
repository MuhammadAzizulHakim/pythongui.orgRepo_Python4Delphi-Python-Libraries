import numpy as np

C = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
L = np.linalg.cholesky(C)

print("Cholesky decomposition:")
print(L)
