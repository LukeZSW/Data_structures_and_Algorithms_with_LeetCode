# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if(preorder == None or inorder == None):
            return None
        else:
            n = len(preorder)
            nn = len(inorder)
            if(n == 0 or nn == 0 or n != nn):
                return None
            else:
                a =  preorder[0]
                root = TreeNode(a)
                self.gettree(root, preorder, inorder)
                return root
    def gettree(self, root, preorder, inorder):
        a = root.val
        nlen = len(preorder)
        n = inorder.index(a)
        if(n>0):
            node1 = TreeNode(preorder[1])
            root.left = node1
            self.gettree(node1, preorder[1:n+1], inorder[0:n])
        if(nlen>n+1):
            a2 =  preorder[n+1]
            node2 = TreeNode(a2)
            root.right = node2
            self.gettree(node2, preorder[n+1:nlen], inorder[n+1:nlen])

        