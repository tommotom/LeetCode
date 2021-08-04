# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []

        ans = []
        def isLeaf(node):
            return not node.left and not node.right

        def helper(node, val, path):
            nonlocal targetSum, ans
            if isLeaf(node) and val == targetSum:
                ans.append([p for p in path])
                return
            if node.left:
                path.append(node.left.val)
                helper(node.left, val+node.left.val, path)
                path.pop()
            if node.right:
                path.append(node.right.val)
                helper(node.right, val+node.right.val, path)
                path.pop()

        helper(root, root.val, [root.val])

        return ans
