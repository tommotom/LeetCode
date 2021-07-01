class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        q = []
        for i in range(n):
            heapq.heappush(q, (-efficiency[i], -speed[i]))
        team = []
        sum_s, ans = 0, 0
        for _ in range(n):
            e, s = heapq.heappop(q)
            e, s = -e, -s
            sum_s += s
            heapq.heappush(team, s)
            if len(team) > k:
                sum_s -= heapq.heappop(team)
            ans = max(ans, sum_s * e)
        return ans % (10**9 + 7)
