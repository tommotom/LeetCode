class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edges = collections.defaultdict(list)
        for v, w in connections:
            edges[v].append(w)
            edges[w].append(v)

        time = 0

        parents = [-1 for _ in range(n)]
        disc = [-1 for _ in range(n)]
        low = [-1 for _ in range(n)]
        ans = []

        def dfs(v):
            nonlocal edges, time, parents, disc, low, ans

            if disc[v] != -1: return

            disc[v] = low[v] = time
            time += 1

            for u in edges[v]:
                if disc[u] == -1:
                    parents[u] = v
                    dfs(u)
                    low[v] = min(low[v], low[u])
                    if low[u] > disc[v]:
                        ans.append([v, u])
                elif parents[v] != u:
                    low[v] = min(low[v], low[u])

        dfs(connections[0][0])

        return ans
