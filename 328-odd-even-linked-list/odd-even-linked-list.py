# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        es = None
        ee = None
        os = None
        oe = None
        temp = head
        length = 0
        while temp:
            length +=1
            temp = temp.next
        curr =  head
        for i in range (1, length+1):
            if i %2 == 0:
                if es is None and ee is None:
                    es = curr
                    ee = curr
                else:
                    ee.next = curr
                    ee = curr
            else:
                if os is None and oe is None:
                    os = curr
                    oe = curr
                else:
                    oe.next = curr
                    oe = curr
            curr = curr.next
        head = os
        oe.next = es
        ee.next = None
        return head

        
        