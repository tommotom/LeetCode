# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {}
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        if root in self.memo: return self.memo[root]

        one = two = 0
        if root.left:
            one += self.rob(root.left)
            two += self.rob(root.left.left)
            two += self.rob(root.left.right)
        if root.right:
            one += self.rob(root.right)
            two += self.rob(root.right.left)
            two += self.rob(root.right.right)

        self.memo[root] = max(one, two + root.val)
        return self.memo[root]
