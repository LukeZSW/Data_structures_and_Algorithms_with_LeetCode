#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : palindrome_pairs.py
@Author  : Siwen
@Time    : 3/9/2020 3:16 PM
"""

"""
336. Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
"""

"""
method1: hashmap
idea:
Given two words s1 and s2, there are two cases when their concatenation may form a palindrome:
Case 1: the reverse of s2 is a suffix of s1 and the rest part of s1 is a palindrome
Case 2: the reverse of s1 is a suffix of s2 and the rest part of s2 is a palindrome
"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = list()
        if not words:
            return res

        d = {w[::-1]: i for i, w in enumerate(words)}

        for i, word in enumerate(words):
            for j in range(len(word)):
                l = word[:j]
                r = word[j:]
                if l in d and d[l] != i and r[::-1] == r:
                    res.append([i, d[l]])
                    if not l:
                        res.append([d[l], i])
                if r in d and d[r] != i and l[::-1] == l:
                    res.append([d[r], i])

        return res

"""
method2: Tire
"""
from collections import defaultdict, deque


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = -1  # reprersent word index in array; -1 means it is not a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, ind):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = ind

    def search(self, word, ind, res, flag):
        if flag == 0:
            word = word[::-1]
            cur = self.root
            for i, c in enumerate(word):
                cur_ind = cur.is_word
                if cur_ind > -1 and cur_ind != ind and self.is_palindromes(word[i:]):
                    res.append([cur_ind, ind])
                if c not in cur.children:
                    return  # quit early
                else:
                    cur = cur.children[c]
            cur_ind = cur.is_word
            if cur_ind > -1 and cur_ind != ind and self.is_palindromes(word[i:]):
                res.append([cur_ind, ind])
        else:
            cur = self.root
            for i, c in enumerate(word):
                cur_ind = cur.is_word
                if cur_ind > -1 and cur_ind != ind and self.is_palindromes(word[i:]):
                    res.append([ind, cur_ind])
                if c not in cur.children:
                    return  # quit early
                else:
                    cur = cur.children[c]

    def is_palindromes(self, s):
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie_pre = Trie()
        trie_suf = Trie()
        for i, word in enumerate(words):
            trie_pre.insert(word, i)
            trie_suf.insert(word[::-1], i)
        res = []
        for i, word in enumerate(words):
            trie_pre.search(word, i, res, 0)
            trie_suf.search(word, i, res, 1)
        return res