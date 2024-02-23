class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, v, c in flights:
            graph[u][v] = c
        cheapest = defaultdict(dict)
        q = [(0, src, k+1)]
        while q:
            cur, u, stop = heapq.heappop(q)
            if stop < 0: continue
            if stop in cheapest[u] and cheapest[u][stop] <= cur: continue
            cheapest[u][stop] = cur
            for v, c in graph[u].items():
                heapq.heappush(q, (cur+c, v, stop-1))
        return min(cheapest[dst].values()) if len(cheapest[dst]) > 0 else -1
