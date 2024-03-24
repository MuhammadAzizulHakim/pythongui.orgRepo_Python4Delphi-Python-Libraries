import numpy as np

A = np.array([[0, 0, 0, 0, 1], [2, 0, 0, 1, 3],
			  [4, 0, 2, 0, 0], [3, 2, 0, 0, 1]],
			dtype=np.float32)

U, S, Vt = np.linalg.svd(A)

print("U (left singular vectors):")
print(U)
print("S (singular values):")
print(S)
print("Vt (right singular vectors):")
print(Vt)
