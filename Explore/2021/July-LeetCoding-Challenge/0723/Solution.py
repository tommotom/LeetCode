# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return

        @lru_cache(None)
        def contains_one(node):
            if not node: return False
            if node.val == 1: return True
            return contains_one(node.left) or contains_one(node.right)

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not contains_one(root.left): root.left = None
        if not contains_one(root.right): root.right = None

        if not root.left and not root.right and root.val == 0: return None
        return root
