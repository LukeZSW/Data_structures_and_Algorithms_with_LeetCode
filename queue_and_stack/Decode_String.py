#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Decode_String.py.py
@Author  : Siwen
@Time    : 2/6/2020 7:43 PM
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num_list = []
        num = ""
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == "]":
                j = len(stack) - 1
                while j >= 0:
                    if stack[j] == "[":
                        break
                    j -= 1
                times = num_list.pop()
                generate_string = "".join(stack[j+1:]) * times
                stack = stack[:j]
                stack.append(generate_string)
                num = ""
            elif s[i] == "[":
                stack.append(s[i])
                num_list.append(int(num))
                num = ""
            else:
                stack.append(s[i])
        return "".join(stack)