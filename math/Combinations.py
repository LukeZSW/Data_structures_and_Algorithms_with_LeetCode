#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Combinations.py
@Author  : Siwen
@Time    : 2/10/2020 10:58 PM
"""

"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

""" 
method 1: library
"""
from itertools import combinations
class Solution:
    def combine(self, nums: List[int]) -> List[List[int]]:
        return list(combinations(range(1, n+1), k))


"""
method 2: recursive
C(n,k) = C(n-1,k-1) + C(n-1,k).
"""
class Solution:
    def combine(self, nums: List[int]) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]


"""
method 3: iterative
C(n,k) = C(n-1,k-1) + C(n-1,k).
"""
class Solution:
    def combine(self, nums: List[int]) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs


"""
method 4: dfs
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, path, res):
            if len(path) == k:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], res)
            return
        nums = [i for i in range(1, n + 1)]
        path = []
        res = []
        dfs(nums, path, res)
        return res