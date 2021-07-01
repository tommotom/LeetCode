# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(node, val, path):
            if node.val == val: return path, True
            if node.left:
                path.append("l")
                path, found = find_path(node.left, val, path)
                if found: return path, True
            if node.right:
                path.append("r")
                path, found = find_path(node.right, val, path)
                if found: return path, True
            path.pop()
            return path, False

        p_path, _ = find_path(root, p.val, [])
        q_path, _ = find_path(root, q.val, [])
        i, j = 0, 0
        while i < len(p_path) and j < len(q_path):
            if p_path[i] == q_path[j] == "l":
                root = root.left
                i += 1
                j += 1
            elif p_path[i] == q_path[j] == "r":
                root = root.right
                i += 1
                j += 1
            else:
                break
        return root
