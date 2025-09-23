# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# 각 요소 더하기
c = a+b

# c= np.add(a, b)
print(c) # [-3 -3 -3]

# 각 요소 곱하기
# c = a*b
# 각 요소 나누기
# c = a/b
c = np.divide(a,b)
print(c) # [0.25 0.4 0.5]

arr1 = [[1,2],[3,4]] #list 변수 선언
arr2 = [[5,6],[7,8]] #list 변소 선언
a = np.array(arr1)
b = np.array(arr2)

c= np.dot(a, b)
print(c)