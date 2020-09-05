# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        def goleft(root, stack):
            while root.left:
                stack.append(root)
                root = root.left
            return root
        root1 = goleft(root1, stack1) if root1 else None
        root2 = goleft(root2, stack2) if root2 else None

        def inorder(root, stack, ret):
            ret.append(root.val)
            if root.right:
                root = goleft(root.right, stack)
            elif stack: root = stack.pop()
            else: root = None
            return root

        ret = []
        while root1 and root2:
            if root1.val < root2.val:
                root1 = inorder(root1, stack1, ret)
            else:
                root2 = inorder(root2, stack2, ret)
        while root1:
            root1 = inorder(root1, stack1, ret)
        while root2:
            root2 = inorder(root2, stack2, ret)
        return ret
