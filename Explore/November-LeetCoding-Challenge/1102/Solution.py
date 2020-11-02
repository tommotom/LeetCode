# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        unsorted = head
        hat = ListNode()

        while unsorted:
            tmp = unsorted
            unsorted = unsorted.next
            tmp.next = None

            node = hat
            while node.next and node.next.val < tmp.val:
                node = node.next

            if not node.next:
                node.next = tmp
                continue

            tmp.next = node.next
            node.next = tmp

        return hat.next
