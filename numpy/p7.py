import numpy as np

arr = np.arange(1, 10) # 1D array
print(arr, '\n')

arr = arr.reshape(3, 3) # 2D array
print(arr, '\n')

arr = arr.reshape(9) # 1D array
print(arr, '\n')

arr = arr.reshape(9, 1) # 2D array
print(arr, '\n')

arr = arr.reshape(1, 9) # 2D aarray
print(arr, '\n')
