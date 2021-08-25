# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        def dfs(node):
            nonlocal visited, k
            if node.val not in visited and k - node.val in visited:
                return True
            visited.add(node.val)
            ret = False
            if node.left:
                ret = ret or dfs(node.left)
            if node.right:
                ret = ret or dfs(node.right)
            return ret
        return dfs(root)
