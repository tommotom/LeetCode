class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]

        if "1" <= s[0] <= "9": dp[0] = 1

        for i in range(1, len(s)):
            if "1" <= s[i] <= "9": dp[i] += dp[i-1]
            if "10" <= s[i-1:i+1] <= "26":
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[-1]
