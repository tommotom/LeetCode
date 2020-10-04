# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root: return False
        q = deque([(0, root)])
        last = -float('inf')
        while q:
            level, node = q.popleft()
            if node.left:
                q.append((level+1, node.left))
            if node.right:
                q.append((level+1, node.right))

            if level % 2 == 0:
                if node.val % 2 == 0: return False
                if last >= node.val: return False
                if q and q[0][0] != level:
                    last = float('inf')
                else:
                    last = node.val
            else:
                if node.val % 2 == 1: return False
                if last <= node.val: return False
                if q and q[0][0] != level:
                    last = -float('inf')
                else:
                    last = node.val

        return True
