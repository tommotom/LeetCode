# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        node = head
        while node:
            value = node.val
            if node.next and node.next.val == value:
                while node and node.val == value: node = node.next
            else:
                tail.next = node
                tail = tail.next
                node = node.next
                tail.next = None

        return dummy.next
