# -*- coding: utf-8 -*-
import numpy as np # numpy 패키지 로드하여 np로 사용
a = [[1,2,3], [4,5,6]] # 리스트에서 행렬생성 , 2차 행렬
b = np.array(a)
print(a)
print(type(a))
print(b)
print(type(b))
print(b.ndim) # 행의 갯수
print(b.shape) # 행, 열 

print(b[0,0])
print(b[0,1])

#배열의 생성
c = np.zeros([2,2])
print(c)
d = np.zeros([5])
print(d)
e = np.ones([2,2])
print(e)
f = np.full([2,3], 5)
print(f)
