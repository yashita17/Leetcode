# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        if head is None or head.next is None:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        slow = head
        while fast != slow:
            slow = slow.next 
            fast = fast.next
        return slow
        
        