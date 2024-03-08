import numpy as np
 
a = np.arange(30).reshape(2, 3, 5)
 
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)