import numpy as np

a1 = np.array([22, 42, 6, 81])
a2 = np.array([12, 92, 33, 56])
a3 = np.array([0, 2, 66])

print(np.hstack((a1, a2, a3))) # The output the method hstack returns is 1D array
print('\n')
print(np.hstack((a3, a1, a2, a1)))