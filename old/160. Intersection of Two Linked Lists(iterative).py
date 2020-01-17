# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        if a == None or b == None:
            return None
        flag1 = 0
        flag2 = 0
        i = 0
        lena = float('inf')
        lenb = float('inf')
        while a != b:
            if a == None:
                if flag1 == 0:
                    flag1 = 1
                    lena = i
                a = headB
            else:
                a = a.next
            if b == None:
                if flag2 == 0:
                    flag2 = 1
                    lenb = i
                b = headA
            else:
                b = b.next
            i += 1
            if i > lena + lenb:
                return None
        return a