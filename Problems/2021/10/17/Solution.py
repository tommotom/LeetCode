# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0

        def helper(node):
            if not node: return []

            if node.left:
                left = helper(node.left)
            else:
                left = []

            if node.right:
                right = helper(node.right)
            else:
                right = []

            for i in range(len(left)):
                left[i] += node.val
                if left[i] == sum: self.ans += 1

            for i in range(len(right)):
                right[i] += node.val
                if right[i] == sum: self.ans += 1

            if node.val == sum: self.ans += 1

            return left + right + [node.val]

        helper(root)
        return self.ans
