class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def dp(node, mask):
            state = (node, mask)
            if state in cache: return cache[state]
            if mask & (mask-1) == 0: return 0

            cache[state] = float('inf')
            for neigh in graph[node]:
                if mask & (1 << neigh):
                    already_visited = 1 + dp(neigh, mask)
                    not_visited = 1 + dp(neigh, mask ^ (1 << node))
                    cache[state] = min(cache[state], already_visited, not_visited)
            return cache[state]

        n = len(graph)
        ending_mask = (1 << n) - 1
        cache = {}
        return min(dp(node, ending_mask) for node in range(n))
