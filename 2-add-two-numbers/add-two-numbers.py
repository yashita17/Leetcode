# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a = l1
        b = l2
        carry = 0
        temp = ListNode(0)
        head = temp
        while a and b:
            sum = a.val + b.val + carry
            temp.val = sum%10
            carry = sum//10
            temp.next = ListNode(0)
            temp = temp.next
            a = a.next
            b = b.next
        if a is None:
            while b:
                sum = b.val + carry
                temp.val = sum %10
                carry = sum//10
                temp.next = ListNode(0)
                temp = temp.next
                b = b.next
        if b is None:
            while a:
                sum = a.val + carry
                temp.val = sum %10
                carry = sum//10
                temp.next = ListNode(0)
                temp = temp.next
                a = a.next
        if carry:
            temp.val = carry
            temp.next = None
        else:
            curr = head
            while curr.next.next:
                curr = curr.next
            curr.next = None
        return head

            
            
        