class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return [i for i in range(n)]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = []
        for k, v in graph.items():
            if len(v) == 1:
                leaves.append(k)

        rest = n
        while rest > 2:
            rest -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves
