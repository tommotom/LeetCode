# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        level = 1
        q = collections.deque([(root,level)])
        ans = []
        while q:
            tmp = []
            while q and q[0][1] == level:
                node = q.popleft()[0]
                tmp.append(node.val)
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))
            ans.append(tmp)
            level += 1
        return ans
