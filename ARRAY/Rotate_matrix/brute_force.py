from typing import *
import numpy as np
def rotateMatrix(mat : List[List[int]]):
    pass
    n = len(mat)
    print(n)

    ans = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):

            ans[j][(n-1)-i] = mat[i][j]
    return ans         
a = [[1,2,3],[4,5,6],[7,8,9]]
b = rotateMatrix(a)
print(b[0][0],a[0][0])