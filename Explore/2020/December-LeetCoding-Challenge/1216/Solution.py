# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        last = None
        stack = []
        node = root

        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack: break
                node = stack.pop()
                if last is not None and not last < node.val: return False
                last = node.val
                node = node.right

        return True