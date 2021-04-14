# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller_head, greater_head = ListNode(), ListNode()
        smaller, greater = smaller_head, greater_head

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
                head = head.next
                smaller.next = None
            else:
                greater.next = head
                greater = greater.next
                head = head.next
                greater.next = None

        smaller.next = greater_head.next
        return smaller_head.next
