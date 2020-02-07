#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : 01_Matrix.py
@Author  : Siwen
@Time    : 2/7/2020 5:45 PM
"""


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        dist = [[float('inf') for _ in range(col)] for _ in range(row)]
        que = collections.deque([])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    que.append([i, j])
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # BFS for each 0
        while len(que) != 0:
            cur_row, cur_col = que.popleft()
            for move_row, move_col in move:
                new_row = cur_row + move_row
                new_col = cur_col + move_col
                if new_row >= 0 and new_row < row and new_col >= 0 and new_col < col:
                    # updat minimal cell
                    if dist[new_row][new_col] > dist[cur_row][cur_col] + 1:
                        dist[new_row][new_col] = dist[cur_row][cur_col] + 1
                        que.append([new_row, new_col])
        return dist
