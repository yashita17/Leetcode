# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums)

        while head and head.val in nums:
            head = head.next

        curr = head

        while curr and curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

        
        