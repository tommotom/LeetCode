class Node:
    l = None
    r = None
    val = None

    def __init__(self, val):
        self.val = val

class Solution:
    def validateBinaryTreeNodes(self, n: int, L: List[int], R: List[int]) -> bool:
        nodes = {}
        parents = defaultdict(list)
        for i in range(n):
            node = Node(i)
            if L[i] >= 0:
                node.l = L[i]
                parents[L[i]].append(i)
            if R[i] >= 0:
                node.r = R[i]
                parents[R[i]].append(i)
            nodes[i] = node

        root = None
        for i in range(n):
            if i not in parents:
                if root: return False
                root = i

        if root is None: return False

        visited = set()
        def dfs(node):
            if node in visited: return False
            visited.add(node)
            if nodes[node].l is not None and not dfs(nodes[node].l): return False
            if nodes[node].r is not None and not dfs(nodes[node].r): return False
            return True

        return dfs(root) and len(visited) == n
