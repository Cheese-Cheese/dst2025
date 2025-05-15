import numpy as np

my_number = int(input('Enter number of your choice: '))

arr2 = np.full((1, 5), my_number)

print(arr2)
print(arr2[0])
print(arr2[0][1])
# print(arr2[1][0]) -- Error since 2nd row doesn't exist
