#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : 01_Matrix.py
@Author  : Siwen
@Time    : 2/7/2020 5:56 PM
"""

"""
Iterate the matrix from top to bottom-left to right:
    Update dist[i][j] = min(dist[i][j], min(dist[i][j-1],  dist[i-1][j]) + 1)
    i.e., minimum of the current dist and distance from top or left neighbour +1, that would have been already calculated previously in the current iteration.
Now, we need to do the back iteration in the similar manner: from bottom to top-right to left:
    Update dist[i][j] = min(dist[i][j], min( dist[i][j+1],  dist[i+1][j]) + 1)
    i.e. minimum of current dist and distances calculated from bottom and right neighbours, that would be already available in current iteration.
Time complexity: O(row * col)
Space complexity: O(row * col).
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        dist = [ [ float('inf') for _ in range(col)] for _ in range(row)]
        # First pass: check for left and top
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # second paas: check for bottom and right
        for i in reversed(range(row)):
            for j in reversed(range(col)):
                if i < row - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < col - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist