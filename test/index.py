import numpy as np

a = np.asarray(range(12))
a = a.reshape([2,2,-1])

print(a[:,:,-2:])