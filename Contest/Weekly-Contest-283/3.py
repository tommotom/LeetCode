# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        num_to_node = {}
        parents = defaultdict(list)
        for parent, child, isLeft in descriptions:
            parents[child].append(parent)

            if not parent in num_to_node:
                num_to_node[parent] = TreeNode(parent)
            if not child in num_to_node:
                num_to_node[child] = TreeNode(child)

            if isLeft == 1:
                num_to_node[parent].left = num_to_node[child]
            else:
                num_to_node[parent].right = num_to_node[child]

        for p, c, i in descriptions:
            if len(parents[p]) == 0:
                return num_to_node[p]
