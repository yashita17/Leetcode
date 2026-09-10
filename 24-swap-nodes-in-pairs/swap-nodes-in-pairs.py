# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        curr = head.next.next
        prev = head
        head = head.next
        head.next = prev
        while curr and curr.next:
            prev.next = curr.next
            prev = curr
            new = curr.next.next
            curr.next.next = prev
            curr = new
        prev.next = curr
        return head


        