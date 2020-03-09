#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : add_and_search_word_data_structure_design.py
@Author  : Siwen
@Time    : 3/5/2020 6:32 PM
"""

"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""

"""
method 1: Tire 
"""
from collections import defaultdict


class TireNode:
    def __init__(self):
        self.children = defaultdict(TireNode)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TireNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        trienode_l = [self.root]
        for c in word:
            temp_l = []
            for node in trienode_l:
                if c == ".":
                    for char, newnode in node.children.items():
                        temp_l.append(newnode)
                if c in node.children:
                    temp_l.append(node.children[c])
            if not temp_l:
                return False
            trienode_l = temp_l
        for node in trienode_l:
            if node.is_word:
                return True
        return False


"""
method 2: save length to word dictionary
because only search exact word, prefix not useful
"""

from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.vocab = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.vocab[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.vocab[len(word)]

        pool = self.vocab[len(word)]
        for i, ch in enumerate(word):
            if ch != '.':
                pool = {wrd for wrd in pool if wrd[i] == ch}
            if not pool:
                return False
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
