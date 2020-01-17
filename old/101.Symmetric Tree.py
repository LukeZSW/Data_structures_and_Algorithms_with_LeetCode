# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        level = [root]
        while level.count(None) != len(level):
            j = 0;
            k = len(level) - 1
            while j <= k:
                if level[j] == None and level[k] != None:
                    return False
                if level[j] != None and level[k] == None:
                    return False
                if level[j] != None and level[k] != None:
                    if level[j].val != level[k].val:
                        return False
                j += 1
                k -= 1
            b = []
            for i in level:
                if i != None:
                    b.append(i.left)
                    b.append(i.right)
            level = b
        return True