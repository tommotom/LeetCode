class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_at = {}
        ans = 0
        for i, char in enumerate(s):
            if char in char_at:
                ans = max(ans, i - char_at[char])
            char_at[char] = i
        return max(ans, len(s))
