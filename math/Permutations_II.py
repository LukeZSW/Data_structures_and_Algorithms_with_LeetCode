#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Permutations_II.py
@Author  : Siwen
@Time    : 2/8/2020 8:02 PM
"""

"""
Problem:  47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

"""
method 1: recursive + unique value
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n == 1: # stop recursive
            return [nums]
        nums.sort()
        unique = list(set(nums))
        unique.sort() # get unique value list
        j = 0
        for i in range(n):
            if j == len(unique):
                break
            if nums[i] == unique[j]: # change unique value only once
                nums[0], nums[i] = nums[i], nums[0]
                per = self.permuteUnique(nums[1:]) # recursive, get the permutations of remaining integers
                for l in per:
                    temp = [nums[0]]
                    temp.extend(l)
                    res.append(temp)
                nums[0], nums[i] = nums[i], nums[0]
                j += 1
        return res


"""
method 2: backtrack with set
use set to avoid same permutations
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(start, end):
            if start == end:
                res.add(tuple(nums[:]))
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0, len(nums))
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res