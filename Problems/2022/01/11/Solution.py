# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node and not node.left and not node.right

        ans = 0
        def helper(node, num):
            nonlocal ans

            if not node: return

            num = num * 2 + node.val
            if isLeaf(node):
                ans += num
                return

            helper(node.left, num)
            helper(node.right, num)

        helper(root, 0)

        return ans
