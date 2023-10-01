class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([])
        for u in range(n):
            if len(graph[u]) == 1:
                q.append(u)

        sums = [0] * n
        ans = 0

        while q:
            u = q.popleft()
            sums[u] += values[u]
            if sums[u] % k == 0:
                ans += 1
                sums[u] = 0
            for v in graph[u]:
                graph[v].remove(u)
                sums[v] += sums[u]
                if len(graph[v]) == 1:
                    q.append(v)

        return max(1, ans)
