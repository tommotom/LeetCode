# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt = 0

        def helper(node):
            nonlocal tilt
            if not node: return 0

            left = helper(node.left)
            right = helper(node.right)

            tilt += abs(right - left)

            return left + right + node.val

        helper(root)

        return tilt
