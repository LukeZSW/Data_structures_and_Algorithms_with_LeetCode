#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : course_schedule(detect_circle).py
@Author  : Siwen
@Time    : 10/1/2019 6:29 PM
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        black = set()
        white = set()
        gray = set()
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
            white.add(a)
        for i in range(numCourses):
            if i in white:
                if self.hasCycle(i, white, gray, black, adj):
                    return False
        return True

    def hasCycle(self, v, white, gray, black, adj):
        white.remove(v)
        gray.add(v)
        for succ in adj[v]:
            if succ in white:
                if self.hasCycle(succ, white, gray, black, adj):
                    return True
            elif succ in gray:
                return True
            elif succ in black:
                continue
        gray.remove(v)
        black.add(v)
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True
        adj = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for a in prerequisites:
            adj[a[1]][a[0]] = 1
            indegree[a[0]] += 1
        q = collections.deque()
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while len(q) > 0:
            i = q.popleft()
            count += 1
            for j in range(numCourses):
                if adj[i][j] == 1:
                    adj[i][j] = 0
                    indegree[j] -= 1

                    if indegree[j] == 0:
                        q.append(j)

        return count == numCourses


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adjtable = [[] for _ in range(numCourses)]
        self.state = [0] * numCourses
        self.valid = [None] * numCourses
        for cur, pre in prerequisites:
            self.adjtable[cur].append(pre)

        for v in range(numCourses):
            if self.exam_valid(v) == False:
                return False
        return True

    def exam_valid(self, course_id):
        if self.valid[course_id] is not None:
            return self.valid[course_id]

        self.state[course_id] = 1  # first makes it active
        for pre in self.adjtable[course_id]:
            if self.state[pre] == 1:
                self.valid[course_id] = False
                return False
            else:
                pre_state = self.exam_valid(pre)
                if pre_state == False:
                    return False
        self.state[course_id] = 0
        self.valid[course_id] = True
        return True