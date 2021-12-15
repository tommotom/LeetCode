# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        sorted_head = head
        node = head
        while node.next:
            if node.next.val < sorted_head.val:
                tmp = node.next.next
                node.next.next = sorted_head
                sorted_head = node.next
                node.next = tmp
                continue

            sorted_node = sorted_head
            while sorted_node.next != node.next and sorted_node.next.val < node.next.val:
                sorted_node = sorted_node.next

            if not sorted_node.next == node.next:
                tmp = node.next.next
                node.next.next = sorted_node.next
                sorted_node.next = node.next
                node.next = tmp
            else:
                node = node.next

        return sorted_head
