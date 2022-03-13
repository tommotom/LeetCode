class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        G1, G2 = defaultdict(list), defaultdict(list)
        for f, t, w in edges:
            G1[f].append((t, w))
            G2[t].append((f, w))

        def dijkstra(graph, src):
            q, t = [(0, src)], {}
            while q:
                time, cur = heappop(q)
                if cur not in t:
                    t[cur] = time
                    for to, w in graph[cur]:
                        heappush(q, (time+w, to))
            return [t[i] if i in t else float('inf') for i in range(n)]

        arr1 = dijkstra(G1, src1)
        arr2 = dijkstra(G1, src2)
        arr3 = dijkstra(G2, dest)

        ans = float('inf')
        for i in range(n):
            ans = min(ans, arr1[i] + arr2[i] + arr3[i])

        return ans if ans < float('inf') else -1
