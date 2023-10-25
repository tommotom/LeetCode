class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for pre, nex in relations:
            graph[pre].append(nex)
            degree[nex] += 1

        q = []
        for i in range(1, n+1):
            if degree[i] == 0:
                heapq.heappush(q, (time[i-1], i))

        while q:
            t, pre = heapq.heappop(q)
            for nex in graph[pre]:
                degree[nex] -= 1
                if degree[nex] == 0:
                    heapq.heappush(q, (t + time[nex-1], nex))
            if not q: return t
