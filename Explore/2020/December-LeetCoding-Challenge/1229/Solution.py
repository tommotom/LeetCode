from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = defaultdict(lambda:0)
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if not root: return 0

        self.count[root.val] += 1

        if not self.isLeaf(root):
            left = self.pseudoPalindromicPaths(root.left)
            right = self.pseudoPalindromicPaths(root.right)
            self.count[root.val] -= 1
            return left + right

        odd = False
        ans = 0
        for c in self.count.values():
            if not c % 2 == 0:
                if odd: break
                odd = True
        else:
            ans = 1
        self.count[root.val] -= 1
        return ans

    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right
