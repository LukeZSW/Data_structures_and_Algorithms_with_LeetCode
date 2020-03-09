#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : word_search_ii.py
@Author  : Siwen
@Time    : 3/7/2020 3:40 PM
"""


"""
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""

"""
method: use tire and dfs
notice: in dfs, reset visited because cells can visited agiain after explored
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    def search(self, board, i, j):
        # DFS
        def dfs(row_ind, col_ind, node, s, res, visited, moves):
            visited[row_ind][col_ind] = 2
            if node.is_word:
                res.add(s)
            for move in moves:
                next_row_ind = row_ind + move[0]
                next_col_ind = col_ind + move[1]
                if 0 <= next_row_ind < row_len and 0 <= next_col_ind < col_len and visited[next_row_ind][
                    next_col_ind] < 2 and board[next_row_ind][next_col_ind] in node.children:
                    dfs(next_row_ind, next_col_ind, node.children[board[next_row_ind][next_col_ind]],
                        s + board[next_row_ind][next_col_ind], res, visited, moves)
            visited[row_ind][col_ind] = 1

        res = set()
        c = board[i][j]
        if c not in self.root.children:
            return res
        row_len, col_len = len(board), len(board[0])
        visited = [[0 for _ in range(col_len)] for _i in range(row_len)]
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dfs(i, j, self.root.children[c], board[i][j], res, visited, moves)
        return res


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0:
            return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        row_len, col_len = len(board), len(board[0])
        res = set()
        for i in range(row_len):
            for j in range(col_len):
                res = res | trie.search(board, i, j)
        return res