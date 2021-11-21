# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, v in enumerate(inorder): inorder_map[v] = i

        def helper(low, high):
            if low > high: return None
            root = TreeNode(postorder.pop())
            mid = inorder_map[root.val]
            root.right = helper(mid+1, high)
            root.left = helper(low, mid-1)
            return root

        return helper(0, len(inorder)-1)
