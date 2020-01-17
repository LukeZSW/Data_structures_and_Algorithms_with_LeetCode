# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if(inorder == None or postorder == None):
            return None
        else:
            n = len(postorder)
            nn = len(inorder)
            if(n == 0 or nn == 0 or n != nn):
                return None
            else:
                a =  postorder[n-1]
                root = TreeNode(a)
                self.gettree(root, inorder, postorder)
                return root
    def gettree(self, root, inorder, postorder):
        a = root.val
        nlen = len(postorder)
        n = inorder.index(a)
        if(n>0):
            inorder1 = inorder[0:n]
            postorder1 = postorder[0:n]
            n1 = len(postorder1)
            a1 =  postorder1[n1-1]
            node1 = TreeNode(a1)
            root.left = node1
            self.gettree(node1, inorder1, postorder1)
        if(nlen-1>n):
            inorder2 = inorder[n+1:nlen]
            postorder2 = postorder[n:nlen-1]
            n2 = len(postorder2)
            a2 =  postorder2[n2-1]
            node2 = TreeNode(a2)
            root.right = node2
            self.gettree(node2, inorder2, postorder2)

        