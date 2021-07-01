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
        prev, first, last = None, None, None

        def traversal(root):
            nonlocal prev, first, last
            if not root: return
            traversal(root.left)
            if prev:
                if prev.val > root.val:
                    if not first: first = prev
                    last = root
            prev = root
            traversal(root.right)

        traversal(root)
        first.val, last.val = last.val, first.val
