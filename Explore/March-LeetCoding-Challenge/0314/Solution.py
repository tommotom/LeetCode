# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        left = head
        for _ in range(k-1): left = left.next

        right = head
        for _ in range(length-k): right = right.next

        left.val, right.val = right.val, left.val

        return head
