# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = ans = None
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack: break
                root = stack.pop()
                if head:
                    ans.right = TreeNode(root.val)
                    ans = ans.right
                else:
                    head = TreeNode(root.val)
                    ans = head
                root = root.right

        return head
