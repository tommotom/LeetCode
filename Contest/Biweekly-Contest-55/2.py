class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        def helper(s):
            nonlocal n, part

            for i in range(len(s)-n+1):
                if s[i:i+n] == part:
                    return helper(s[:i]+s[i+n:])
            return s
        return helper(s)
