class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        def circle(u):
            visited = set()
            while u not in visited:
                visited.add(u)
                u = edges[u]
            for v in visited:
                ans[v] = len(visited)

        def dfs(u):
            if ans[u] == 0:
                ans[u] = dfs(edges[u]) + 1
            return ans[u]

        n = len(edges)
        ans = [0] * n
        degs = [0] * n
        for u, v in enumerate(edges):
            degs[v] += 1

        for u, d in enumerate(degs):
            if ans[u] > 0: continue
            if d > 1:
                l, r = u, edges[u]
                while l != r:
                    l = edges[l]
                    r = edges[r]
                    r = edges[r]
                circle(l)

        for u, d in enumerate(degs):
            if ans[u] > 0: continue
            if d == 0: dfs(u)

        for u, d in enumerate(degs):
            if ans[u] > 0: continue
            if d == 1: circle(u)

        return ans
