# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def dfs(node):
            nonlocal arr
            if not node: return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)

        ans = []
        for q in queries:
            i = bisect.bisect_left(arr, q)
            if i == len(arr):
                l = arr[i-1]
            elif i == 0:
                l = arr[i] if arr[i] == q else -1
            else:
                l = arr[i-1] if arr[i] > q else arr[i]
            r = arr[i] if i < len(arr) else -1
            ans.append([l, r])
        return ans
