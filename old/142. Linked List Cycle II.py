# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            slow = fast = head
            meet = False
            while fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    meet = True
                    break
            if meet == False:
                return None
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow