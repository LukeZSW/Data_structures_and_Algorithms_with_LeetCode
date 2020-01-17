# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levelOrder = [root]
        result = []
        while levelOrder:
            vals = []
            nextLevel = []
            for node in levelOrder:
                if node:
                    vals.append(node.val)
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
            if vals != []:
                result.append(vals)
            levelOrder = nextLevel
        return result