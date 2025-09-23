# -*- coding: utf-8 -*-
import numpy as np
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
a = arr[0:2, 0:2]
print(a)

import numpy as np
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
a = arr[0:2, 0:2]
print(a)
b = arr[1:, 1:]
print(b)
