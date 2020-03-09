#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : maximum_xor_of_two_numbers_in_an_array.py.py
@Author  : Siwen
@Time    : 3/6/2020 6:55 PM
"""

"""
421. Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

"""
method1: find prefix directly not use tire; delete useless node
res += any(res ^ 1 ^ p in prefixes for p in prefixes)
Need to make a note for my future self.

The key idea is just build the maximal answer bit by bit, so that we want to add a '1' to every bit, but without changing the previous bits.
By using XOR, how do we get 1: just find two numbers, one has a 1 on this bit, the other has 0 (or they are opposite on this bit).
How do we guarantee that these two numbers are exactly the same two who construct the previous part of this answer? If we denote the two numbers as a and b, then the previous answer shall be a^b. 
We also know a and b should exist in the set prefix, and a ^ b ^ a = b. The next part is fairly simple: using just try answer ^ a for all a in prefix, if the result still exists in prefix, then the result must be b.

So actually this res ^ 1 ^ p test two things:

find the two elements in nums that constructs the previous answer
check this two elements have opposite bits at current position
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(32)[::-1]:
            res <<= 1
            prefixes = {num >> i for num in nums}
            res += any(res ^ 1 ^ p in prefixes for p in prefixes)
        return res


"""
method 2: Tire, use Tire find max for every nums in nums
"""
from collections import defaultdict


class TireNode:
    def __init__(self):
        self.children = defaultdict(TireNode)


class Trie:
    def __init__(self):
        self.root = TireNode()

    def insert(self, num):
        cur = self.root
        for i in range(32):
            tmp = num & 1 << (31 - i)
            if tmp:
                cur = cur.children[1]
            else:
                cur = cur.children[0]

    def find_max(self, num):
        res = 0
        cur = self.root
        for i in range(32):
            tmp = num & 1 << (31 - i)
            if tmp:
                if 0 in cur.children:
                    res += 1 << (31 - i)
                    cur = cur.children[0]
                else:
                    cur = cur.children[1]
            else:
                if 1 in cur.children:
                    res += 1 << (31 - i)
                    cur = cur.children[1]
                else:
                    cur = cur.children[0]
        return res


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return 0
        trie = Trie()
        for num in nums:
            trie.insert(num)
        res = 0
        for num in nums:
            res = max(res, trie.find_max(num))
        return res



"""
method 3: Tire, search in Tire
"""
from collections import defaultdict


class TireNode:
    def __init__(self):
        self.children = defaultdict(TireNode)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TireNode()

    def insert(self, l):
        cur = self.root
        for num in l:
            cur = cur.children[num]
        cur.is_end = True

    def find(self):
        def getmaxl(temp1, temp2):
            for i in range(len(temp1)):
                if temp1[i] > temp2[i]:
                    return temp1
                elif temp2[i] > temp1[i]:
                    return temp2
            return temp1

        def help(node1, node2, l):
            if len(node1.children) == 0:
                return
            if 1 in node1.children and 0 in node1.children:
                l.append(1)
                if 1 in node2.children and 0 in node2.children:
                    temp1 = []
                    temp2 = []
                    help(node1.children[1], node2.children[0], temp1)
                    help(node1.children[0], node2.children[1], temp2)
                    l.extend(getmaxl(temp1, temp2))
                else:
                    if 1 in node2.children:
                        help(node1.children[0], node2.children[1], l)
                    else:
                        help(node1.children[1], node2.children[0], l)
            else:
                if 1 in node1.children:
                    if 0 in node2.children:
                        l.append(1)
                        help(node1.children[1], node2.children[0], l)
                    else:
                        l.append(0)
                        help(node1.children[1], node2.children[1], l)
                else:
                    if 1 in node2.children:
                        l.append(1)
                        help(node1.children[0], node2.children[1], l)
                    else:
                        l.append(0)
                        help(node1.children[0], node2.children[0], l)

        l = []
        cur = self.root
        while True:
            if 1 in cur.children and 0 in cur.children:
                l.append(1)
                break
            else:
                l.append(0)
                if 1 in cur.children:
                    cur = cur.children[1]
                else:
                    cur = cur.children[0]
        help(cur.children[1], cur.children[0], l)
        res = 0
        for i in range(len(l)):
            res = res * 2 + l[i]
        return res


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def get_bin(num):
            bin_list = []
            while num > 0:
                bin_list.append(num % 2)
                num = num // 2
            while len(bin_list) < 32:
                bin_list += [0]
            bin_list.reverse()
            return bin_list

        nums = list(set(nums))
        if len(nums) == 1:
            return 0
        trie = Trie()
        for num in nums:
            trie.insert(get_bin(num))
        res = trie.find()
        return res


"""
method 4: get max from all possible results
time: O(nlgn)
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return 0
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, nums[i] ^ nums[j])
        return res