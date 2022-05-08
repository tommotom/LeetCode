# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node: return 0, 0
            l_sum, l_count = helper(node.left)
            r_sum, r_count = helper(node.right)

            c_sum = l_sum + r_sum + node.val
            c_count = l_count + r_count + 1

            if node.val == c_sum // c_count:
                ans += 1

            return c_sum, c_count
        helper(root)
        return ans
