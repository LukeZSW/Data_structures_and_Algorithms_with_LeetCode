#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Perfect_Squares.py
@Author  : Siwen
@Time    : 1/24/2020 7:20 PM
"""

from collections import deque



class Solution:
    def numSquares(self, n: int) -> int:
        d = deque([0])
        step = -1
        s = set()
        while len(d) > 0:
            size = len(d)
            step += 1
            for i in range(size):
                a = d.popleft()
                j = 1
                while (a + j * j) <= n:
                    if (a + j * j) in s:
                        j += 1
                        continue
                    if (a + j * j) == n:
                        return step + 1
                    d.append(a + j ** 2)
                    s.add(a + j ** 2)
                    j += 1
        return 0