#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Valid_Parentheses.py.py
@Author  : Siwen
@Time    : 2/3/2020 3:33 PM
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
