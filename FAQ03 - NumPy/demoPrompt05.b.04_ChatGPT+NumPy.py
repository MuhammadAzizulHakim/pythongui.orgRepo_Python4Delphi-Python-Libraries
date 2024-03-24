import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5]])

Q, R = np.linalg.qr(A)

print("Q (orthogonal matrix):")
print(Q)
print("R (upper triangular matrix):")
print(R)
