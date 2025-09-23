# -*- coding: utf-8 -*-
import numpy as np
a = np.array([[-1,2,3],[3,4,8]])
s = np.sum(a)
print('sum=',a.sum()) 

print('sum ny row=',a,sum(axis=0)) #행 방향
print('sum ny row=',a,sum(axis=1)) #열 방향