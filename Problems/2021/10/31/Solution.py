"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def helper(head):
            node = tail = head
            while node:
                if node.child:
                    child_head, child_tail = helper(node.child)
                    node.child = None
                    tmp = node.next
                    node.next = child_head
                    child_head.prev = node
                    if tmp:
                        tmp.prev = child_tail
                    child_tail.next = tmp
                    node = child_tail
                tail = node
                node = node.next

            return head, tail

        return helper(head)[0]
