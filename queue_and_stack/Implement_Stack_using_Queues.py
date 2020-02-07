#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : Implement_Stack_using_Queues.py
@Author  : Siwen
@Time    : 2/6/2020 7:22 PM
"""

from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for i in range(len(self.queue)):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return - 1
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        value = self.queue.popleft()
        return value

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return - 1
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        value = self.queue[0]
        self.queue.append(self.queue.popleft())
        return value

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()