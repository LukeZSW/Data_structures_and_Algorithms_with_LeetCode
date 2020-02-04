#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Evaluate_Reverse_Polish_Notation.py.py
@Author  : Siwen
@Time    : 2/3/2020 4:35 PM
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(token))
        return stack[0]
