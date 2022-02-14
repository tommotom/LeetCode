# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        st = []
        node = root
        ans = depth = 1
        while True:
            while node:
                st.append((node, depth))
                node = node.left
                depth += 1
            if st:
                node, depth = st.pop()
                ans = max(ans, depth)
                node = node.right
                depth += 1
            else:
                break
        return ans
