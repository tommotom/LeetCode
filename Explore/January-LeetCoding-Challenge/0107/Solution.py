class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_at = {}
        ans = 0
        duplicated_at = -1
        for i, char in enumerate(s):
            if char in char_at:
                duplicated_at = max(duplicated_at, char_at[char])
            ans = max(ans, i - duplicated_at)
            char_at[char] = i
        return ans
