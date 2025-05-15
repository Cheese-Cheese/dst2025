import numpy as np

a1 = np.array([22, 42, 6, 81])
a2 = np.array([12, 92, 33, 56])
a3 = np.array([0, 2, 66, 71])

print(np.vstack((a1, a2, a3)))
print('\n')
print(np.vstack((a3, a1, a2, a1)))