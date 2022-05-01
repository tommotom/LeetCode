class Solution:
    def appealSum(self, s: str) -> int:
        seen_at = defaultdict(int)
        seen_at[s[0]] = 1
        appeal = 1
        ans = 1
        for i in range(1, len(s)):
            appeal += 1 + i - seen_at[s[i]]
            seen_at[s[i]] = i + 1
            ans += appeal
        return ans
