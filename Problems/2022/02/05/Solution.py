# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = deque(lists)
        while len(q) > 1:
            head1 = q.popleft()
            head2 = q.popleft()
            head = ListNode(0)
            merged = head

            while head1 and head2:
                if head1.val > head2.val:
                    merged.next = head2
                    merged = merged.next
                    head2 = head2.next
                else:
                    merged.next = head1
                    merged = merged.next
                    head1 = head1.next

            if head1:
                merged.next = head1
            elif head2:
                merged.next = head2

            q.append(head.next)

        if q:
            return q.popleft()
        else:
            return None
