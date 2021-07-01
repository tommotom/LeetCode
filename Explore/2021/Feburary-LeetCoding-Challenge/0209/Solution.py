# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        larger = 0
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.right
            else:
                if not stack: break
                node = stack.pop()
                tmp = node.val
                node.val += larger
                larger += tmp
                node = node.left

        return root
