# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def levelOf(node, val, cur):
            if not node: return

            if node.val == val: return cur

            return levelOf(node.left, val, cur+1) or levelOf(node.right, val, cur+1)

        def parentOf(node, val):
            if not node: return

            if node.left and node.left.val == val: return node
            if node.right and node.right.val == val: return node

            return parentOf(node.left, val) or parentOf(node.right, val)

        return (levelOf(root, x, 0) == levelOf(root, y, 0)) and (parentOf(root, x) != parentOf(root, y))
