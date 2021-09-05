class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n, mod = len(nextVisit), 10**9 + 7
        dp = [0] * n
        for i in range(1, n):
            dp[i] = (2*(dp[i-1] + 1) - dp[nextVisit[i-1]]) % mod
        return dp[-1]
