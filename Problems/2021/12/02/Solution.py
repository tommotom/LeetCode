# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        odd_head = head
        even_dummy_head = ListNode(0)

        odd, even = odd_head, even_dummy_head
        while odd and odd.next:
            even.next = odd.next
            odd.next = odd.next.next

            even = even.next
            even.next = None

            if odd.next:
                odd = odd.next

        odd.next = even_dummy_head.next

        return odd_head
