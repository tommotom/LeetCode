# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return

        node, length = head, 1
        while node.next:
            length += 1
            node = node.next
        k %= length

        if k == 0: return head

        newhead = head
        for _ in range(length - k - 1):
            newhead = newhead.next
        tmp = newhead
        newhead = newhead.next
        tmp.next = None

        node = newhead
        while node.next:
            node = node.next

        node.next = head

        return newhead
