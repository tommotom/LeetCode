# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length <= 2: return

        mid = head
        for _ in range(math.ceil(length/2)-1):
            mid = mid.next
        tmp = mid.next
        mid.next = None
        mid = tmp

        new_head = mid
        while mid.next:
            tmp = mid.next
            mid.next = mid.next.next
            tmp.next = new_head
            new_head = tmp

        node = head
        while new_head:
            tmp1 = node.next
            node.next = new_head
            tmp2 = new_head.next
            new_head.next = tmp1
            new_head = tmp2
            node = tmp1
