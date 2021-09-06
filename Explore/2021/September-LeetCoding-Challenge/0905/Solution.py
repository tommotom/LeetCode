class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for i in range(1, len(s)):
                ans = min(ans, s[i:] + s[:i])
        else:
            ans = "".join(sorted(s))
        return ans
