# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans, idx = [], 0
        if not root: return ans

        def helper(node):
            nonlocal ans, idx
            if not node or (ans and ans[-1] == -1):
                idx -= 1
                return
            if node.val != voyage[idx]:
                ans.append(-1)
                return

            if node.right and node.right.val == voyage[idx+1] and node.left:
                ans.append(node.val)
                idx += 1
                helper(node.right)
                idx += 1
                helper(node.left)
            else:
                idx += 1
                helper(node.left)
                idx += 1
                helper(node.right)

        helper(root)
        if ans and ans[-1] == -1: return[-1]
        return ans
