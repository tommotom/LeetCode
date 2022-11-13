# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        ans = 0
        while q:
            level = q[0][1]
            nodes = []
            while q and q[0][1] == level:
                node = q.popleft()[0]
                nodes.append(node.val)
                if node.left: q.append((node.left, level+1))
                if node.right: q.append((node.right, level+1))

            org = {}
            for i, node in enumerate(nodes):
                org[node] = i

            sorted_nodes = sorted(nodes)
            i = 0
            while i < len(nodes):
                s, n = sorted_nodes[i], nodes[i]
                if s != n:
                    nodes[i], nodes[org[s]] = s, n
                    org[n], org[s] = org[s], org[n]
                    ans += 1
                i += 1

        return ans
