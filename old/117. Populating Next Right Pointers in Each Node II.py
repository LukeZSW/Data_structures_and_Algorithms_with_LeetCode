# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.findNextAvail(root)
        if root.right:
            if root.next:
                root.right.next = self.findNextAvail(root)
        self.connect(root.right) 
        self.connect(root.left)

    def findNextAvail(self,root):
        if root.next:
            if root.next.left:
                return root.next.left
            elif root.next.right:
                return root.next.right
            else:
                return self.findNextAvail(root.next)
        else:
            return None