# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        ans = 0
        def helper(root):
            nonlocal ans
            if not root: return 0

            l_sum = helper(root.left)
            r_sum = helper(root.right)

            ans += abs(l_sum - r_sum)
            return l_sum + r_sum + root.val

        helper(root)

        return ans
