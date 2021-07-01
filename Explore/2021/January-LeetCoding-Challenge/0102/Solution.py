from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q1 = deque([original])
        q2 = deque([cloned])

        while True:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 == target: return node2

            if node1.left:
                q1.append(node1.left)
                q2.append(node2.left)

            if node1.right:
                q1.append(node1.right)
                q2.append(node2.right)
