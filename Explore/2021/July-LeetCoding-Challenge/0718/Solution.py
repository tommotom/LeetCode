# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head):
            tail = head
            stack = []
            while tail.next:
                stack.append(tail)
                tail = tail.next
            new_head = tail
            while stack:
                tail.next = stack[-1]
                tail = stack.pop()
            tail.next = None
            return new_head, tail

        def helper(head):
            if not head: return
            node = head
            for _ in range(k-1):
                node = node.next
                if not node: break
            else:
                tmp = node.next
                node.next = None
                rev_head, rev_tail = reverse(head)
                rev_tail.next = helper(tmp)
                return rev_head
            return head

        return helper(head)
