class Solution:
    def partitionString(self, s: str) -> int:
        seen = [False] * 26
        ans = 1
        for c in s:
            i = ord(c) - ord('a')
            if seen[i]:
                seen = [False] * 26
                ans += 1
            seen[i] = True
        return ans
