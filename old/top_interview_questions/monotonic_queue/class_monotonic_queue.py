#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : class_monotonic_queue.py
@Author  : Siwen
@Time    : 9/26/2019 10:27 PM
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
