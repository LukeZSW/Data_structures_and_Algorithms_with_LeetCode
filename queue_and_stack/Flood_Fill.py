#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Flood_Fill.py
@Author  : Siwen
@Time    : 2/6/2020 8:02 PM
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        stack = [[sr, sc]]
        color = image[sr][sc]
        visited = [[0 for _ in range(col)] for _ in range(row)]
        while len(stack) > 0:
            cr, cc = stack.pop()
            image[cr][cc] = newColor
            if cr - 1 >= 0 and image[cr - 1][cc] == color and visited[cr - 1][cc] == 0:
                stack.append([cr - 1, cc])
                visited[cr - 1][cc] = 1
            if cr + 1 < row and image[cr + 1][cc] == color and visited[cr + 1][cc] == 0:
                stack.append([cr + 1, cc])
                visited[cr + 1][cc] = 1
            if cc - 1 >= 0 and image[cr][cc - 1] == color and visited[cr][cc - 1] == 0:
                stack.append([cr, cc - 1])
                visited[cr][cc - 1] = 1
            if cc + 1 < col and image[cr][cc + 1] == color and visited[cr][cc + 1] == 0:
                stack.append([cr, cc + 1])
                visited[cr][cc + 1] = 1
        return image