# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,0)])
        ans = 0
        while q:
            new_level = deque([])
            base = q[0][1]
            begin = end = 0
            while q:
                node, pos = q.popleft()
                pos -= base
                begin = min(begin, pos)
                end = max(end, pos)
                if node.left: new_level.append((node.left, 2*pos))
                if node.right: new_level.append((node.right, 2*pos+1))
            ans = max(ans, end-begin+1)
            q = new_level
        return ans
