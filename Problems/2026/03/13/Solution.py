class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        q = []
        for (i, w) in enumerate(workerTimes):
            heapq.heappush(q, (w, i, 2))
        while True:
            (w, i, n) = heapq.heappop(q)
            mountainHeight -= 1
            if mountainHeight == 0: return w
            heapq.heappush(q, (w + workerTimes[i] * n, i, n + 1))
        return 0
