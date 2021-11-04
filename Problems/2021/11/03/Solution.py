# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def isLeaf(node):
            return node and node.left == None and node.right == None

        def helper(node, val):
            nonlocal ans
            if not node: return

            val = 10 * val + node.val

            if isLeaf(node):
                ans += val
                return

            helper(node.left, val)
            helper(node.right, val)

        helper(root, 0)

        return ans
