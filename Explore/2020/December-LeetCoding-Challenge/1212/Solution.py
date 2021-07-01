# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return

        @lru_cache(maxsize=None)
        def childDepth(root):
            if not root: return -1
            left = childDepth(root.left)
            right = childDepth(root.right)
            return max(left, right) + 1

        left = childDepth(root.left)
        right = childDepth(root.right)
        if left > right: return self.subtreeWithAllDeepest(root.left)
        elif left < right: return self.subtreeWithAllDeepest(root.right)
        return root
