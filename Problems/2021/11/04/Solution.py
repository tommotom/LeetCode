# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def isLeaf(node):
            return node and not node.left and not node.right

        def hasLeftLeaf(node):
            return node and node.left and isLeaf(node.left)

        ans = 0
        def helper(node):
            nonlocal ans
            if not node: return
            if hasLeftLeaf(node):
                ans += node.left.val
            helper(node.left)
            helper(node.right)

        helper(root)
        return ans
