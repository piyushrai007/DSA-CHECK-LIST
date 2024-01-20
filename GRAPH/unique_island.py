import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        def isValid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1
        
        def dfs(i, j, vis, arr):
            vis[i][j] = True
            arr.append((i, j))
            
            refX = [-1, 0, 0, 1]
            refY = [0, 1, -1, 0]
            
            for x, y in zip(refX, refY):
                nodeX = i + x
                nodeY = j + y
                if isValid(nodeX, nodeY):
                    if not vis[i+x][j+y]:
                        dfs(nodeX, nodeY, vis, arr)
            return
        
        m, n = len(grid), len(grid[0])
        vis = [[False]*n for _ in range(m)]
        distinctIslands = set()
        
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    arr = []
                    dfs(i, j, vis, arr)
                    # print(arr)
                    for k in range(len(arr)):
                        x, y = arr[k]
                        ele = (x-i, y-j)
                        arr[k] = ele
                    # print(arr)
                    distinctIslands.add(tuple(arr))
        return len(distinctIslands)