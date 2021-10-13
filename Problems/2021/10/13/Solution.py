# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder.pop(0))
        if not preorder: return root
        idx = 0
        while idx < len(preorder) and preorder[idx] < root.val:
            idx += 1
        root.left = self.bstFromPreorder(preorder[:idx])
        root.right = self.bstFromPreorder(preorder[idx:])
        return root
