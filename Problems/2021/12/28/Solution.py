# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        node = head
        for _ in range(length//2):
            node = node.next

        return node
