#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : DFS_template.py
@Author  : Siwen
@Time    : 11/12/2019 1:35 PM
"""

from collections import deque

# iterate version


# recursive version


# search in a 2D grid
# Given a 2D grid consists of 0 and 1(barriers)
# 4 direction left, top, right, bottom
# get longest depth
def dfs_grid(grid):
    # grid: List[List[int]]
    m, n = len(grid), len(grid[0])
    max_depth = 0
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]
    for begin_i in range(m):
        for begin_j in range(n):
            if grid[begin_i][begin_j] == 0:
                stack = [[begin_i, begin_j, 1]]
                while len(stack) > 0:
                    cur_i, cur_j, cur_depth = stack.pop()
                    if cur_i < 0 or cur_i >= m or cur_j < 0 or cur_j >= n:
                        continue
                    if grid[cur_i][cur_j] == 1:
                        continue
                    max_depth = max(max_depth, cur_depth)
                    for k in range(4):
                        stack.append([cur_i + di, cur_j + dj, cur_depth + 1])
    return max_depth


def dfs_recursive(grid, i, j, d)


def bfs_grid(grid):
    # grid: List[List[int]]
    m, n = len(grid), len(grid[0])
    max_depth = 0
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]
    for begin_i in range(m):
        for begin_j in range(n):
            if grid[begin_i][begin_j] == 0:
                deq = deque([[begin_i, begin_j, 1]])
                while len(deq) > 0:
                    cur_i, cur_j, cur_depth = deq.popleft()
                    if cur_i < 0 or cur_i >= m or cur_j < 0 or cur_j >= n:
                        continue
                    if grid[cur_i][cur_j] == 1:
                        continue
                    max_depth = max(max_depth, cur_depth)
                    for k in range(4):
                        deq.append([cur_i + di, cur_j + dj, cur_depth + 1])
    return max_depth
