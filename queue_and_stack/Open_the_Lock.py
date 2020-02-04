#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Open_the_Lock.py
@Author  : Siwen
@Time    : 1/17/2020 9:36 PM
"""

from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        if target in deadends or "0000" in deadends:
            return -1
        step = -1
        d = deque(["0000"])
        visited.add("0000")
        while len(d) > 0:
            size = len(d)
            step += 1
            for i in range(size):
                s = d.popleft()
                if s == target:
                    return step
                l = [s[i] for i in range(len(s))]
                for j in range(4):
                    temp = l[j]
                    l[j] = str((int(temp) + 1) % 10)
                    news = ''.join(l)
                    if news not in deadends and news not in visited:
                        d.append(news)
                        visited.add(news)
                    l[j] = str((int(temp) + 9) % 10)
                    news = ''.join(l)
                    if news not in deadends and news not in visited:
                        d.append(news)
                        visited.add(news)
                    l[j] = temp
        return -1
