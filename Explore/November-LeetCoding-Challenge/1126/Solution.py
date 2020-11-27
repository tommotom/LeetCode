from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0

        count = Counter(s)
        length = len(s)

        if min(count.values()) >= k: return length

        i, j = 0, 0
        ans = 0
        while j < length:
            if count[s[j]] < k:
                ans = max(ans, self.longestSubstring(s[i:j], k))
                j += 1
                i = j
            else:
                j += 1
        return max(ans, self.longestSubstring(s[i:j], k))
