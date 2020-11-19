class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        ans = ""
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit(): j += 1
                num = int(s[i:j])
                level = 1
                j += 1
                start = j
                while level:
                    if s[j] == "[": level += 1
                    elif s[j] == "]": level -= 1
                    j += 1
                ans += num * self.decodeString(s[start:j-1])
                i = j
            else:
                ans += s[i]
                i += 1
        return ans
