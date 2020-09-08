# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root: return 0

        stack = [(root, [])]
        ans = 0

        while stack:
            node, path = stack.pop()
            path.append(str(node.val))
            if not node.left and not node.right:
                ans += int("".join(path), 2)
            else:
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))
        return ans
