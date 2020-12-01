from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        q = deque([(1, root)])
        ans = 0
        while q:
            depth, node = q.popleft()
            ans = max(depth, ans)
            if node.left: q.append((depth+1, node.left))
            if node.right: q.append((depth+1, node.right))

        return ans
