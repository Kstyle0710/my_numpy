'''
"Numpy" is short for "Numerical Python"
'''

import numpy as np

## 1차원 배열 생성
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print(type(a1))
print(a1.shape)
print(a1[3])


## 2차원 배열 생성
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a2)
print(type(a2))
print(a2.shape)
print(a2[0][1])
