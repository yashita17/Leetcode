# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        len1 = 0
        len2 = 0
        curr1 = headA
        while curr1:
            curr1 = curr1.next
            len1 +=1
        curr2 = headB
        while curr2:
            curr2 = curr2.next
            len2 +=1
        n = abs(len1 - len2)
        temp1 = headA
        temp2 = headB
        if len1 > len2:
            while  n> 0:
                temp1 = temp1.next
                n -=1
        else:
            while n>0:
                temp2 = temp2.next
                n -=1
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None
        