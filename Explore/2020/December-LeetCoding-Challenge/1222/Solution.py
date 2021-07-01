# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(node):
            if not node: return 0, True
            l_depth, l_balanced = helper(node.left)
            r_depth, r_balanced = helper(node.right)
            return max(l_depth, r_depth) + 1, l_balanced and r_balanced and abs(l_depth - r_depth) < 2

        return helper(root)[1]
