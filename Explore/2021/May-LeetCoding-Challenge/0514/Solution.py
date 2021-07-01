# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root: return None, None

            if root.left and root.right:
                l_head, l_tail = helper(root.left)
                r_head, r_tail = helper(root.right)
                root.right = l_head
                l_tail.right = r_head
                root.left = None
                tail = r_tail
            elif root.left:
                l_head, l_tail = helper(root.left)
                root.right = l_head
                root.left = None
                tail = l_tail
            elif root.right:
                r_head, r_tail = helper(root.right)
                root.right = r_head
                tail = r_tail
            else:
                tail = root

            return root, tail

        helper(root)
