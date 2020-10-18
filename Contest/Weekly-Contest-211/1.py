class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic, ans = {}, -1
        for i, char in enumerate(s):
            if char in dic: ans = max(ans, i - dic[char] - 1)
            else: dic[char] = i
        return ans
