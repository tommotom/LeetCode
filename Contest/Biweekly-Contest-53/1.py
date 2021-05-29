class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        cur = collections.defaultdict(int)
        cur[s[0]] += 1
        cur[s[1]] += 1
        ans = 0
        for i in range(2, len(s)):
            cur[s[i]] += 1
            if len(cur) == 3:
                ans += 1
            cur[s[i-2]] -= 1
            if cur[s[i-2]] == 0:
                del cur[s[i-2]]
        return ans
