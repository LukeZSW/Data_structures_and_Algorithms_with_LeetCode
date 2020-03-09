#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : map_sum_pairs.py
@Author  : Siwen
@Time    : 3/5/2020 5:46 PM
"""

"""
677. Map Sum Pairs

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""

from collections import defaultdict, deque


class TireNode:
    def __init__(self):
        self.children = defaultdict(TireNode)
        self.is_word = False
        self.value = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            cur = cur.children[c]
        cur.is_word = True
        cur.value = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        # BFS
        val_sum = 0
        deq = deque([cur])
        while deq:
            node = deq.popleft()
            if node.is_word:
                val_sum += node.value
            for key, next_node in node.children.items():
                deq.append(next_node)
        return val_sum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)