# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node = headA
        while node:
            node.val *= -1
            node = node.next

        node = headB
        ans = None
        while node:
            if not ans and node.val < 0:
                ans = node
            node.val *= -1
            node = node.next

        node = headA
        while node:
            node.val *= -1
            node = node.next

        node = headB
        while node:
            node.val *= -1
            node = node.next

        return ans
