class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        dp = [0] * len(s)

        for i in range(k-1, len(s)):
            if i > 0: dp[i] = dp[i-1]
            l = k
            while i-l+1 >= 0:
                left, right = i-l+1, i
                valid = True
                while left < right:
                    if s[left] != s[right]:
                        valid = False
                        break
                    left += 1
                    right -= 1

                if valid:
                    dp[i] = max(dp[i], (dp[i-l] if i-l >= 0 else 0) + 1)
                    break
                l += 1
        return dp[-1]
