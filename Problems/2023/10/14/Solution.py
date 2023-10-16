class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        rest = list(time)
        for i in range(n-2, -1, -1):
            rest[i] += rest[i+1]

        @lru_cache(None)
        def dp(i, t):
            if i == n: return 0 if t >= 0 else float('inf')
            if t >= n - i: return 0
            if t + rest[i] < 0: return float('inf')
            return min(dp(i+1, t-1), cost[i] + dp(i+1, t + time[i]))

        return dp(0, 0)
