# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(nodes, odd):
            if not nodes or nodes[0] == None: return

            if odd:
                nums = [node.val for node in nodes]
                for node, num in zip(nodes, nums[::-1]):
                    node.val = num

            next_nodes = []
            for node in nodes:
                next_nodes.append(node.left)
                next_nodes.append(node.right)

            helper(next_nodes, not odd)

        helper([root], False)
        return root
