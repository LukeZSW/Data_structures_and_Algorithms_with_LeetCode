#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : replace_words.py
@Author  : Siwen
@Time    : 3/5/2020 5:58 PM
"""

"""
648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
 

Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    def searchPrefix(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        prefix = ''
        cur = self.root
        for c in word:
            if cur.is_word:
                return prefix
            if c not in cur.children:
                return word
            prefix += c
            cur = cur.children[c]
        return word


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        tire = Trie()
        for word in dict:
            tire.insert(word)
        words_list = sentence.split(" ")
        for i in range(len(words_list)):
            words_list[i] = tire.searchPrefix(words_list[i])
        return " ".join(words_list)