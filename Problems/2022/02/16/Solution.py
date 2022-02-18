# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        node = dummy

        while node and node.next and node.next.next:
            tmp = node.next
            node.next = node.next.next
            node = node.next

            tmp.next = node.next
            node.next = tmp
            node = node.next

        return dummy.next
