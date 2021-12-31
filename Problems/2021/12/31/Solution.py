# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def helper(node):
            nonlocal ans
            c_max = c_min = node.val

            if node.left:
                l_max, l_min = helper(node.left)
                ans = max(ans, abs(node.val - l_max))
                ans = max(ans, abs(node.val - l_min))
                c_max = max(c_max, l_max)
                c_min = min(c_min, l_min)

            if node.right:
                r_max, r_min = helper(node.right)
                ans = max(ans, abs(node.val - r_max))
                ans = max(ans, abs(node.val - r_min))
                c_max = max(c_max, r_max)
                c_min = min(c_min, r_min)

            return c_max, c_min

        helper(root)

        return ans
