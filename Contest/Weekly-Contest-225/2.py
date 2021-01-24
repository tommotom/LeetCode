from collections import Counter

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        c1 = Counter(ord(c) - 97 for c in a)
        c2 = Counter(ord(c) - 97 for c in b)
        res = m + n - max((c1+c2).values())
        for i in range(25):
            c1[i+1] += c1[i]
            c2[i+1] += c2[i]
            res = min(res, m - c1[i] + c2[i])
            res = min(res, n - c2[i] + c1[i])
        return res
