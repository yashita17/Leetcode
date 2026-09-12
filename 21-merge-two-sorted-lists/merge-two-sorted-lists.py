# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        a = list1
        b = list2
        tail = ListNode(0)
        head = tail
        while a and b:
            if a.val <= b.val:
                tail.next = a
                tail = a
                a = a.next
            else:
                tail.next = b
                tail = b
                b = b.next
        if a != None:
            tail.next = a
            
        if b != None:
            tail.next = b
        head = head.next
        return head
        
        