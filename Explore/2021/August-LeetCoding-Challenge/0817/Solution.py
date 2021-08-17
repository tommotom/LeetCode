# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        ans = 0
        def dfs(node, maxValue):
            nonlocal ans
            maxValue = max(maxValue, node.val)
            if maxValue == node.val:
                ans += 1
            if node.left:
                dfs(node.left, maxValue)
            if node.right:
                dfs(node.right, maxValue)
        dfs(root, root.val)
        return ans
