# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        LL1 = set()
        while temp1:
            LL1.add(temp1)
            temp1 = temp1.next
        temp2 = headB
        while temp2:
            if temp2 in LL1:
                return temp2
            temp2 = temp2.next
        return None

        