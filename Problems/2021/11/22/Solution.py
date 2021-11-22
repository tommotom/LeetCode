# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if root.val == key:
            if not root.right:
                return root.left

            tmp = root.right
            if not tmp.left:
                tmp.left = root.left
                return tmp

            while tmp.left and tmp.left.left:
                tmp = tmp.left

            new_root = tmp.left
            tmp.left = new_root.right
            new_root.right = root.right
            new_root.left = root.left
            root = new_root

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root
