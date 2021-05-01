class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i, c in enumerate(s):
            if i % 2 == 0:
                ans += c
            else:
                ans += chr(ord(s[i-1]) + int(c))
        return ans
