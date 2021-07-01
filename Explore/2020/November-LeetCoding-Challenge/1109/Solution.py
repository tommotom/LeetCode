# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root: return 0

        def helper(node):
            max_ancestor = min_ancestor = node.val
            if node.left:
                left_max, left_min, left_ans = helper(node.left)
                max_ancestor = max(max_ancestor, left_max)
                min_ancestor = min(min_ancestor, left_min)
            if node.right:
                right_max, right_min, right_ans = helper(node.right)
                max_ancestor = max(max_ancestor, right_max)
                min_ancestor = min(min_ancestor, right_min)

            ans = max(abs(max_ancestor - node.val), abs(min_ancestor - node.val))

            if node.left:
                ans = max(ans, left_ans)
            if node.right:
                ans = max(ans, right_ans)

            return max_ancestor, min_ancestor, ans

        max_ancestor, min_ancestor, ans = helper(root)
        return ans
