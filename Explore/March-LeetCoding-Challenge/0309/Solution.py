# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root or d < 1: return root
        if d == 1: return TreeNode(v, root, None)

        def helper(node, v, d, isRight):
            if d == 1:
                if isRight: return TreeNode(v, None, node)
                else: return TreeNode(v, node, None)
            if d < 1 or not node: return node

            node.left = helper(node.left, v, d-1, False)
            node.right = helper(node.right, v, d-1, True)
            return node

        root.left = helper(root.left, v, d-1, False)
        root.right = helper(root.right, v, d-1, True)

        return root
