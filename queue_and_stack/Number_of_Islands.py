#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Number_of_Islands.py
@Author  : Siwen
@Time    : 1/17/2020 8:47 PM
"""

# BFS
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid:
            return res
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    res += 1
                    d = deque([[i, j]])
                    while len(d) > 0:
                        size = len(d)
                        for k in range(size):
                            a, b = d.popleft()
                            visited[a][b] = 1
                            if a - 1 >= 0 and grid[a-1][b] == '1' and visited[a-1][b] == 0:
                                d.append([a-1, b])
                            if b - 1 >= 0 and grid[a][b-1] == '1' and visited[a][b-1] == 0:
                                d.append([a, b-1])
                            if a + 1 < m and grid[a+1][b] == '1' and visited[a+1][b] == 0:
                                d.append([a+1, b])
                            if b + 1 < n and grid[a][b+1] == '1' and visited[a][b+1] == 0:
                                d.append([a, b+1])
        return res


# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid:
            return res
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    res += 1
                    stack = [[i, j]]
                    while len(stack) > 0:
                        a, b = stack.pop()
                        visited[a][b] = 1
                        if a - 1 >= 0 and grid[a - 1][b] == '1' and visited[a - 1][b] == 0:
                            stack.append([a - 1, b])
                        if b - 1 >= 0 and grid[a][b - 1] == '1' and visited[a][b - 1] == 0:
                            stack.append([a, b - 1])
                        if a + 1 < m and grid[a + 1][b] == '1' and visited[a + 1][b] == 0:
                            stack.append([a + 1, b])
                        if b + 1 < n and grid[a][b + 1] == '1' and visited[a][b + 1] == 0:
                            stack.append([a, b + 1])
        return res
