# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return None
        while head and head.val == val:
            head = head.next
        temp1 = head
        if temp1 is None:
            return head
        temp2 = temp1.next
        while temp2:
            if temp2.val == val:
                temp1.next = temp2.next
                temp2 = temp1.next
            else:
                temp1 = temp2
                temp2 = temp2.next
        return head

        