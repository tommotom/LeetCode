class Solution:
    def minFlips(self, s: str) -> int:
        if len(s) % 2 == 0:
            c1, c2 = "0", "1"
            p1, p2 = 0, 0
            for i in range(len(s)):
                if s[i] != c1: p1 += 1
                if s[i] != c2: p2 += 1
                c1, c2 = c2, c1
            return min(p1, p2)
        else:
            c1, c2 = "0", "1"
            p1, p2 = [0] * len(s), [0] * len(s)
            for i in range(len(s)):
                if i > 0:
                    p1[i], p2[i] = p1[i-1], p2[i-1]
                if s[i] != c1:
                    p1[i] += 1
                if s[i] != c2:
                    p2[i] += 1
                c1, c2 = c2, c1
            ans = min(p1[-1], p2[-1])
            for i in range(1,len(s)):
                ans = min(ans, p1[-1]-p1[i]+p2[i-1], p2[-1]-p2[i]+p1[i-1])

            return ans
