# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head

        length = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            length += 1

        tmp = head
        for _ in range(length//2-1):
            tmp = tmp.next

        latter = self.sortList(tmp.next)
        tmp.next = None
        former = self.sortList(head)

        new_head = ListNode()
        tail = new_head

        while former and latter:
            if former.val < latter.val:
                tail.next = former
                former = former.next
            else:
                tail.next = latter
                latter = latter.next
            tail = tail.next
            tail.next = None

        if former: tail.next = former
        if latter: tail.next = latter

        return new_head.next
