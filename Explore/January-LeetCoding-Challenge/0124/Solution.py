# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        if len(lists) == 1: return lists[0]
        left = self.mergeKLists(lists[:len(lists)//2])
        right = self.mergeKLists(lists[len(lists)//2:])

        dummyHead = ListNode(0)
        node = dummyHead
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
            node.next = None
        if left: node.next = left
        if right: node.next = right

        return dummyHead.next
