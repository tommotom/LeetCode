# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        node1, node2 = root1, root2
        while node1:
            stack1.append(node1)
            node1 = node1.left
        while node2:
            stack2.append(node2)
            node2 = node2.left

        ans = []
        while True:
            if not node1:
                if not stack1: break
                node1 = stack1.pop()
            if not node2:
                if not stack2: break
                node2 = stack2.pop()

            if node2.val < node1.val:
                ans.append(node2.val)
                node2 = node2.right
                while node2:
                    stack2.append(node2)
                    node2 = node2.left
            else:
                ans.append(node1.val)
                node1 = node1.right
                while node1:
                    stack1.append(node1)
                    node1 = node1.left

        while True:
            if not node1:
                if not stack1: break
                node1 = stack1.pop()

            ans.append(node1.val)
            node1 = node1.right

            while node1:
                stack1.append(node1)
                node1 = node1.left

        while True:
            if not node2:
                if not stack2: break
                node2 = stack2.pop()

            ans.append(node2.val)
            node2 = node2.right

            while node2:
                stack2.append(node2)
                node2 = node2.left

        return ans
