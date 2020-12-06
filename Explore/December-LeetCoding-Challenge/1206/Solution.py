from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return

        q = deque([(0, root)])
        while q:
            level, node = q.popleft()
            if q and q[0][0] == level: node.next = q[0][1]
            if node.left: q.append((level+1, node.left))
            if node.right: q.append((level+1, node.right))
        return root
