class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def calcHash(s, length):
            mod = (1 << 61) - 1
            base = 26
            p = pow(26, length) % mod
            val = 0
            for c in s[:length]:
                val *= base
                val += ord(c) - ord('a')
                val %= mod

            visited = set([val])
            for i in range(length, len(s)):
                val *= base
                val -= (ord(s[i-length]) - ord('a')) * p
                val += ord(s[i]) - ord('a')
                val %= mod

                if val in visited:
                    return s[i-length+1:i+1]
                visited.add(val)

            return ""

        l, r = 1, len(s)

        while l < r:
            m = (l+r) // 2
            if calcHash(s, m):
                l = m+1
            else:
                r = m

        return calcHash(s, l-1)
