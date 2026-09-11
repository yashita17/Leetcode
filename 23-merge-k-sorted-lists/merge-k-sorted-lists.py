# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            dummy = ListNode(0)
            tail = dummy
            a= head
            b = lists[i]
            while a and b:
                if a.val <= b.val:
                    tail.next = a
                    tail = a
                    a = a.next
                else:
                    tail.next = b
                    tail = b
                    b = b.next
            if a is None:
                tail.next = b
            if b is None:
                tail.next = a
            head = dummy.next
        return head
            

        