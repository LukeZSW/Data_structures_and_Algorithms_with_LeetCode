#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Next_Permutation.py
@Author  : Siwen
@Time    : 2/10/2020 6:49 PM
"""

"""
Problem:  47. Permutations II

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]: # find first decreasing element
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return
        k = i - 1    #  the first decreasing position
        while nums[j] <= nums[k]: # find the smallest element which is larger than first decreasing element
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  # change value
        l, r = k + 1, len(nums) - 1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return