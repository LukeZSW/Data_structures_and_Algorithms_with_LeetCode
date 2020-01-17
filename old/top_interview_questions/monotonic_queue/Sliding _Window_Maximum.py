#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Sliding _Window_Maximum.py
@Author  : Siwen
@Time    : 9/27/2019 12:30 AM
"""

import collections


class Monoqueue:
    def __init__(self):
        self.m_deque = collections.deque()

    # [a, b]
    # a: the actual value,
    # b: how many elements were deleted between it and the one before it.

    def push(self, val):
        count = 0
        while len(self.m_deque) > 0 and self.m_deque[-1][0] < val:
            count += self.m_deque[-1][1] + 1
            self.m_deque.pop()
        self.m_deque.append([val, count])

    def getmax(self):
        return self.m_deque[0][0]

    def pop(self):
        if self.m_deque[0][1] > 0:
            self.m_deque[0][1] -= 1
            return
        self.m_deque.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        mq = Monoqueue()
        res = []
        for i in range(n):
            if i < k - 1:
                mq.push(nums[i])
            else:
                mq.push(nums[i])
                res.append(mq.getmax())
                mq.pop()
        return res

