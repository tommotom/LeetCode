# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []

        def traversal(node):
            nonlocal inorder
            if not node: return
            traversal(node.left)
            inorder.append(node.val)
            traversal(node.right)

        traversal(root)
        inorder.sort()

        idx = 0

        def rewrite(node):
            nonlocal inorder, idx
            if not node: return
            rewrite(node.left)
            node.val = inorder[idx]
            idx += 1
            rewrite(node.right)

        rewrite(root)
