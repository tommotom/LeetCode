class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0 for _ in range(len(s)+1)]
        dp[-1] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "*":
                dp[i] += 9 * dp[i+1]
            elif s[i] != "0":
                dp[i] += dp[i+1]

            if i == len(s) - 1: continue

            if s[i] == "1" or s[i] == "*":
                if s[i+1] == "*":
                    dp[i] += 9 * dp[i+2]
                else:
                    dp[i] += dp[i+2]

            if s[i] == "2" or s[i] == "*":
                if s[i+1] == "*":
                    dp[i] += 6 * dp[i+2]
                elif s[i+1] < "7":
                    dp[i] += dp[i+2]

            dp[i] %= mod
        return dp[0]
