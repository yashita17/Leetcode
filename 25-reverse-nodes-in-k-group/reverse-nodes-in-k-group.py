# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if head == None:
            return head
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count+=1
        if count <k:
            return head
        curr = head
        count = 0
        prev = None
        while curr!= None and count < k:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            count +=1
        if nextNode is not None:
            reverseHead = self.reverseKGroup(nextNode, k)
            head.next = reverseHead
        return prev


        
        