class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(original)):
            graph[original[i]].append((changed[i], cost[i]))

        @lru_cache(None)
        def bfs(f, t):
            q = [(0, f)]
            reachedAt = {}
            while q:
                cur, u = heapq.heappop(q)
                if u == t: return cur
                if u in reachedAt and reachedAt[u] <= cur: continue
                reachedAt[u] = cur
                for v, cost in graph[u]:
                    if v in reachedAt and reachedAt[v] <= cur + cost: continue
                    heapq.heappush(q, (cur + cost, v))
            return None

        ans = 0
        for i in range(len(source)):
            tmp = bfs(source[i], target[i])
            if tmp == None: return -1
            ans += tmp

        return ans
