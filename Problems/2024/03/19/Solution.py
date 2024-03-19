class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = []
        for k, v in Counter(tasks).items():
            heapq.heappush(q, (-v, k, -100))

        t = 0
        while q:
            arr = []
            while q and t - q[0][2] <= n:
                arr.append(heapq.heappop(q))
            if q:
                c, k, last = heapq.heappop(q)
                if c < -1:
                    heapq.heappush(q, (c+1, k, t))
                t += 1
            else:
                t = min([n + a[2] for a in arr]) + 1
            for a in arr:
                heapq.heappush(q, a)
        return t
