class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        length = len(s)
        for i in range(length):
            ans += 1
            left = right = i
            while 0 <= left - 1 and right + 1 < length:
                if s[left - 1] == s[right + 1]:
                    ans += 1
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(length-1):
            left, right = i, i + 1
            while 0 <= left and right < length:
                if s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
                else:
                    break

        return ans
