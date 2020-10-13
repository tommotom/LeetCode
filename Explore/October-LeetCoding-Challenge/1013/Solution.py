# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        hat = ListNode()
        hat.next = head
        self.quickSort(hat, None)
        return hat.next

    def quickSort(self, hat, tail):
        if hat.next is tail or hat.next.next is tail: return

        hat1, hat2, hat3 = hat, hat.next, ListNode()
        tail1, tail2, tail3 = hat1, hat2, hat3
        p, pivot = hat2.next, hat2.val
        while p is not tail:
            if p.val < pivot:
                tail1.next, tail1, p = p, p, p.next
            elif p.val == pivot:
                tail2.next, tail2, p = p, p, p.next
            else:
                tail3.next, tail3, p = p, p, p.next

        tail3.next = tail
        tail2.next = hat3.next
        tail1.next = hat2

        self.quickSort(hat1, hat2)
        self.quickSort(tail2, tail)