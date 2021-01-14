# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1 = 0
        node = l1
        while node:
            len1 += 1
            node = node.next

        len2 = 0
        node = l2
        while node:
            len2 += 1
            node = node.next

        if len2 > len1:
            l1, l2 = l2, l1

        l1_head = l1

        l1.val += l2.val
        carry = l1.val // 10
        l1.val %= 10

        while l2.next:
            l1 = l1.next
            l2 = l2.next

            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10

        while carry:
            if l1.next:
                l1 = l1.next
                l1.val += carry
                carry = l1.val // 10
                l1.val %= 10
            else:
                l1.next = ListNode(carry)
                carry = 0

        return l1_head
