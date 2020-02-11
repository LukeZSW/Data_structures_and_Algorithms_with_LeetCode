#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Permutations.py
@Author  : Siwen
@Time    : 2/8/2020 6:34 PM
"""

"""
Problem: 46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

"""
method 1: backtrack
every time change first num to other num and then recover
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                res.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0, len(nums))
        return res


"""
method 2: DFS
use DFS and record paths
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums_list, path, res):
            if len(nums_list) == 0:
                res.append(path)
            for i in range(len(nums_list)):
                dfs(nums_list[:i] + nums_list[i + 1:], path + [nums_list[i]], res)
        res = []
        path = []
        dfs(nums, path, res)
        return res


"""
method 3: recursive
select one integers and then get the permutations of remaining integers
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n == 1: # stop recursive
            return [nums]
        for i in range(n):
            nums[0], nums[i] = nums[i], nums[0]
            per = self.permute(nums[1:]) # recursive, get the permutations of remaining integers
            for l in per:
                temp = [nums[0]]
                temp.extend(l)
                res.append(temp)
            nums[0], nums[i] = nums[i], nums[0]
        return res