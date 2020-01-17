# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        if not root:
            return answer
        stacknode = []
        node = root
        while node != None:
            stacknode.append(node)
            node = node.left
        while stacknode:
            a = stacknode.pop()
            answer.append(a.val)
            a = a.right
            while a != None:
                stacknode.append(a)
                a = a.left
        return answer