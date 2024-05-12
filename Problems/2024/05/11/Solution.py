class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ans = float('inf')
        cur = 0
        arr = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)], key = lambda x: x[0])

        q = []
        for i in range(n):
            heapq.heappush(q, -arr[i][1])
            cur += arr[i][1]

            if len(q) > k:
                cur += heapq.heappop(q)

            if len(q) == k:
                ans = min(ans, cur * arr[i][0])

        return ans
