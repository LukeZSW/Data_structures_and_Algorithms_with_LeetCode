#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Daily_Temperatures.py.py
@Author  : Siwen
@Time    : 2/3/2020 4:24 PM
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T) # length
        res = [0 for _ in range(n)]
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res
