#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Maximum_Product_of_Splitted_Binary_Tree.py
@Author  : Siwen
@Time    : 2/3/2020 3:24 PM
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums = []

        def fn(node):
            if not node:
                return 0
            ans = node.val + fn(node.left) + fn(node.right)
            sums.append(ans)
            return ans

        total = fn(root)
        return max((x * (total - x)) for x in sums) % (10 ** 9 + 7)
