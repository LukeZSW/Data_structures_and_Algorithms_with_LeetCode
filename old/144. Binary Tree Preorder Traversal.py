# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        if not root:
            return answer
        stacknode = [root]
        while stacknode:
            a = stacknode.pop()
            answer.append(a.val)
            for child in [a.right, a.left]:
                if child:
                    stacknode.append(child)
        return answer
        