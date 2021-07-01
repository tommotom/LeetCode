# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0

        def helper(node):
            nonlocal ans
            if not node: return 2
            l, r = helper(node.left), helper(node.right)
            if l == 0 or r == 0:
                ans += 1
                return 1
            return 2 if l == 1 or r == 1 else 0

        return (helper(root) == 0) + ans
