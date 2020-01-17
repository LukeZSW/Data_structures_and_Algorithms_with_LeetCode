# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
            answer.insert(0, a.val)
            for child in [a.left, a.right]:
                if child:
                    stacknode.append(child)
        return answer