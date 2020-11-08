# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = 0

        node = l1
        while node:
            num1 = 10 * num1 + node.val
            node = node.next

        node = l2
        while node:
            num2 = 10 * num2 + node.val
            node = node.next

        num = str(num1 + num2)
        dummy = ListNode(0)
        node = dummy
        for n in num:
            node.next = ListNode(n)
            node = node.next

        return dummy.next
