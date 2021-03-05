from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        q = deque([(root, 0)])
        ans = []
        level = 0
        while q:
            whole = 0
            count = 0
            while q and q[0][1] == level:
                node, l = q.popleft()
                whole += node.val
                count += 1

                if node.left: q.append((node.left, l + 1))
                if node.right: q.append((node.right, l + 1))
            if count > 0:
                ans.append(whole/count)
            level += 1
        return ans
