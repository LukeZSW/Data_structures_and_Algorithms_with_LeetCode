#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Sliding_Puzzle.py
@Author  : Siwen
@Time    : 2/11/2020 8:34 PM
"""
from typing import List

"""
773. Sliding Puzzle
Hard

493

17

Add to List

Share
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""


"""
BFS + hash
general solution not only for 2 x 3 array
"""
from collections import deque
from copy import deepcopy
from typing import List
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def changeToTuple(mat):
            lis = []
            for l in mat:
                lis.extend(l)
            return tuple(lis)
        m, n = len(board), len(board[0])
        solved = [i for i in range(1, m * n + 1)]
        solved[-1] = 0
        solved = tuple(solved)
        i = j = flag = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    flag = 1
                    break
            if flag == 1:
                break
        deq = deque([[i, j, board]])
        begin_tup = changeToTuple(board)
        step = 0
        if solved == begin_tup:
            return step
        visited = set()
        visited.add(begin_tup)
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while deq:
            size = len(deq)
            step += 1
            for i in range(size):
                cur_r, cur_c, cur_board = deq.popleft()
                for move_r, move_c in moves:
                    next_r = cur_r + move_r
                    next_c = cur_c + move_c
                    if 0 <= next_r < m and 0 <= next_c < n:
                        next_board = deepcopy(cur_board)
                        next_board[next_r][next_c] = cur_board[cur_r][cur_c]
                        next_board[cur_r][cur_c] = cur_board[next_r][next_c]
                        next_tup = changeToTuple(next_board)
                        if next_tup == solved:
                            return step
                        if next_tup not in visited:
                            visited.add(next_tup)
                            deq.append([next_r, next_c, next_board])
        return -1

if __name__ == '__main__':
    m = 3
    n = 4
    test = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            test[i][j] = i * n + j + 1
    test[m - 1][n - 3] = 0
    test[m - 1][n - 2] = m * n - 2
    test[m - 1][n - 1] = m * n - 1
    s = Solution()
    print(s.slidingPuzzle(test))
