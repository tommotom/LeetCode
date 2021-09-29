# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def get_n_elements(head, n):
            if not head: return None, None
            node = head
            for _ in range(n-1):
                node = node.next

            next_head = None
            if node:
                next_head = node.next
                node.next = None
            return head, next_head

        ans = []

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        n, mod = length//k, length%k
        for _ in range(k):
            node, next_head = get_n_elements(head, n+1 if mod >= 1 else n)
            mod -= 1
            ans.append(node)
            head = next_head

        return ans
