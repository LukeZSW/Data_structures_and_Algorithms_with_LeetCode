#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Keys_and_Rooms.py
@Author  : Siwen
@Time    : 2/7/2020 6:14 PM
"""


# DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        open_room = [0 for _ in range(N)]
        stack = [0]
        open_room[0] = 1
        while len(stack) > 0:
            cur = stack.pop()
            for nex in rooms[cur]:
                if open_room[nex] == 0:
                    stack.append(nex)
                    open_room[nex] = 1
        return sum(open_room) == N
