# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(node):
            if not node: return 0
            return max(dfs(node.left), dfs(node.right)) + 1


        leftPath = dfs(root.left)
        rightPath = dfs(root.right)

        return max(leftPath+rightPath, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
