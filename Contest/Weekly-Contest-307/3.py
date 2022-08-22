# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        graph = defaultdict(list)
        p = None
        def build(node):
            nonlocal graph, p
            if not node: return
            if node.val == start: p = node
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
            build(node.left)
            build(node.right)
        build(root)

        visited = set()
        def dfs(node):
            if not node: return -1
            visited.add(node)
            ret = -1
            for g in graph[node]:
                if g not in visited:
                    ret = max(ret, dfs(g))
            return ret + 1

        return dfs(p)
