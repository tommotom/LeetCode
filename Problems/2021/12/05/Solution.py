# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache(None)
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        child = self.rob(root.left) + self.rob(root.right)

        grand_child = 0
        if root.left:
            grand_child += self.rob(root.left.left)
            grand_child += self.rob(root.left.right)
        if root.right:
            grand_child += self.rob(root.right.left)
            grand_child += self.rob(root.right.right)

        return max(child, grand_child + root.val)
