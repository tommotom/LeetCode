# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        if not head.next: return TreeNode(head.val)

        slow = fast = head
        fast = fast.next

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        parent = TreeNode(slow.next.val)
        parent.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        parent.left = self.sortedListToBST(head)

        return parent
