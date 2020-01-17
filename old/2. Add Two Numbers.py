# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        m = l1.val + l2.val
        a = m / 10
        b = m % 10
        root = ListNode(b)
        l3 = root
        while l1.next != None and l2.next != None:
            l1 = l1.next
            l2 = l2.next
            m = l1.val + l2.val + a
            a = m / 10
            b = m % 10
            l3.next = ListNode(b)
            l3 = l3.next
        if l1.next == None and l2.next == None:
            if a != 0:
                l3.next = ListNode(a)
        elif l1.next == None:
            while l2.next != None:
                l2 = l2.next
                m = l2.val + a
                a = m / 10
                b = m % 10
                l3.next = ListNode(b)
                l3 = l3.next
            if a != 0:
                l3.next = ListNode(a)
        elif l2.next == None:
            while l1.next != None:
                l1 = l1.next
                m = l1.val + a
                a = m / 10
                b = m % 10
                l3.next = ListNode(b)
                l3 = l3.next
            if a != 0:
                l3.next = ListNode(a)
        return root
                
                
                
                
        
        