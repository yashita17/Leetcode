# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n+=1
        k = k % n
        temp1 = head
        temp2 = head
        for i in range(n-(k+1)):
            temp2 = temp2.next
        for i in range(n-1):
            temp1 = temp1.next
        temp1.next = head
        head = temp2.next
        temp2.next = None
        return head


        