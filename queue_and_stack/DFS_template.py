#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : DFS_template.py
@Author  : Siwen
@Time    : 2/3/2020 4:41 PM
"""

# Recursion
"""
Return true if there is a path from cur to target.
"""
boolean DFS(Node cur, Node target, Set<Node> visited) {
    return true if cur is target;
    for (next : each neighbor of cur) {
        if (next is not in visited) {
            add next to visted;
            return true if DFS(next, target, visited) == true;
        }
    }
    return false;
}

# Iteration
"""
Return true if there is a path from cur to target.
"""
boolean DFS(int root, int target) {
    Set<Node> visited;
    Stack<Node> stack;
    add root to stack;
    while (s is not empty) {
        Node cur = the top element in stack;
        remove the cur from the stack;
        return true if cur is target;
        for (Node next : the neighbors of cur) {
            if (next is not in visited) {
                add next to visited;
                add next to stack;
            }
        }
    }
    return false;
}