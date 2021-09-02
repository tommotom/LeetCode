# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generateTrees(start, end):
            if start > end: return [None]
            if start == end: return [TreeNode(start)]
            ret = []
            for num in range(start, end+1):
                lefts = generateTrees(start, num-1)
                rights = generateTrees(num+1, end)
                for left in lefts:
                    for right in rights:
                        root = TreeNode(num)
                        root.left = left
                        root.right = right
                        ret.append(root)
            return ret

        return generateTrees(1, n)
