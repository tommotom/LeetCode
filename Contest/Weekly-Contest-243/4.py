class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        eps = 1e-9

        n = len(dist)
        dp = [[10**10] * (n+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i, d in enumerate(dist,1):
            dp[i][0] = ceil(d/speed + dp[i-1][0] - eps)
            for j in range(1, i+1):
                dp[i][j] = min(ceil(d/speed + dp[i-1][j] - eps), d/speed + dp[i-1][j-1])

        for skip, t in enumerate(dp[-1]):
            if t <= hoursBefore:
                return skip
        return -1
