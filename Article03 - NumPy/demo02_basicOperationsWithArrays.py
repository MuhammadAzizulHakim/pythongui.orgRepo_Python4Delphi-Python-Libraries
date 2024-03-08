import numpy as np
 
arr = np.array([7, 10, 3, 11, 29, 15, 18])
print(np.sort(arr))
 
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([7, 8, 9, 10, 11, 12])
print(np.concatenate((a, b)))
 
c = a.reshape(3, 2)
print(c)