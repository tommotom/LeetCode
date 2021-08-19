# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def postOrderTraversal(node):
            nonlocal sums

            leftVal = postOrderTraversal(node.left) if node.left else 0
            rightVal = postOrderTraversal(node.right) if node.right else 0

            tmp = node.val + leftVal + rightVal
            sums.append(tmp)
            return tmp

        postOrderTraversal(root)
        total = sums[-1]

        ans = 1
        for p in sums:
            ans = max(ans, p * (total-p))
        return ans % (10**9 + 7)
