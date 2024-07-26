class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for f, t, w in edges:
            graph[f].append((t, w))
            graph[t].append((f, w))

        minNum = n
        ans = -1

        for i in range(n):
            q = [(-distanceThreshold, i)]
            visited = set()
            while q:
                d, cur = heapq.heappop(q)
                if cur in visited: continue
                visited.add(cur)
                for t, w in graph[cur]:
                    if t in visited: continue
                    if d + w > 0: continue
                    heapq.heappush(q, (d+w, t))
            if len(visited) <= minNum:
                minNum = len(visited)
                ans = i

        return ans
