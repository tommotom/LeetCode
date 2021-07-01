# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        node = dummy
        for _ in range(left-1):
            node = node.next
        rev_head = rev_tail = node.next
        for _ in range(right-left):
            tmp = rev_tail.next
            rev_tail.next = tmp.next
            node.next = tmp
            tmp.next = rev_head
            rev_head = tmp
        return dummy.next
