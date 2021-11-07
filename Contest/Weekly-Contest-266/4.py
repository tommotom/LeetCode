class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        u_to_v = defaultdict(dict)
        for u, v, time in edges:
            u_to_v[u][v] = time
            u_to_v[v][u] = time

        q = deque([(0, 0, [])])
        valid_paths = []
        while q:
            u, time, paths = q.popleft()
            paths.append(u)

            if u == 0:
                valid_paths.append([p for p in paths])

            for v, t in u_to_v[u].items():
                if time+t <= maxTime:
                    q.append((v, time+t, [p for p in paths]))

        ans = 0
        for paths in valid_paths:
            visited = set()
            quality = 0
            for p in paths:
                if not p in visited:
                    quality += values[p]
                visited.add(p)
            ans = max(ans, quality)

        return ans
