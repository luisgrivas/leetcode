# 54 Spiral Matrix
[Problem](https://leetcode.com/problems/spiral-matrix/). Given an m x n matrix, return all elements of the matrix in spiral order.

TODO EX

```python3
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        pos = (0,0)
        dr = (0,1)
        wall = [(0,n), (m,n-1), (m-1,-1)]
        res = []
        while pos not in wall:
            i,j = pos
            res.append(matrix[i][j])
            wall.append(pos)
            if  (dr[0] + i, dr[1] + j) in wall:
                dr = (dr[1], -dr[0])
            pos = (dr[0] + i, dr[1] + j)
        return res
```
