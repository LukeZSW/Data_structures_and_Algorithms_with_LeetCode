#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Permutation_Sequence.py
@Author  : Siwen
@Time    : 2/10/2020 7:37 PM
"""

"""
60. Permutation Sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        nums = []
        fac = 1
        for i in range(1, n + 1):
            nums.append(i)
            fac = fac * i
        k -= 1
        # select number and then remove it in nums
        for i in range(n):
            fac = fac // (n - i)
            s = k // fac
            num = nums[s]
            nums.remove(num)
            res += str(num)
            k -= s * fac
        return res